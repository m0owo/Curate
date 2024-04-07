from .s_info_ui import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from .seller_order_box_ui import Ui_OrderBox
from .seller_product_box_ui import Ui_ProductBox
from .paying_ui import Ui_Dialog as Ui_confirm
import socket, pickle
from PySide6.QtGui import *
import os
from PIL import Image
import socket
import time
import traceback
import datetime
import shutil
from promptpay import qrcode

class OrderBox(QFrame):
    def __init__(self, order_details, server_host, server_port, parent=None):
        QFrame.__init__(self, None)
        self.ui = Ui_OrderBox()
        self.ui.setupUi(self)
        self.server_host = server_host
        self.server_port = server_port

        self.order_details = order_details

        self.product_name = order_details.get('product_name')
        self.buyer = order_details.get('order_buyer')
        self.order_id = order_details.get('order_id')
        self.price = order_details.get('price')
        self.order_date = order_details.get('order_date')
        self.order_status = order_details.get('order_status')
        self.slip_path = order_details.get('slip_picture')
        image_path = order_details.get('images')
        self.pixmap = QPixmap(image_path)

        self.ui.product_image_label.setPixmap(self.pixmap)
        self.ui.buyer_name.setText("Buyer: " + self.buyer)
        self.ui.product_name.setText(self.product_name)
        self.ui.order_id_label.setText(str(self.order_id))
        self.ui.order_date_label.setText("Order Date: " + self.order_date.strftime("%Y-%m-%d %H:%M:%S"))
        self.ui.price_label.setText("Price: " + str(self.price) + " B")
        self.ui.status_label.setText("Status: " + self.order_status)

        if self.order_status == "unpaid":
            self.ui.confirm_button.setText("Confirm Payment")
        elif self.order_status == "shipping":
            self.ui.confirm_button.setText("Confirm Shipping")
        elif self.order_status == "completed":
            self.ui.confirm_button.setText("Completed")

        self.ui.confirm_button.clicked.connect(self.confirm_status)

    def confirm_status(self):
        confime_payment = Paying(self.slip_path, self.order_details, self.server_host, self.server_port)
        confime_payment.exec_()
        pass

class ProductBox(QFrame):
    def __init__(self, order_details, parent=None):
        QFrame.__init__(self, None)
        self.order_details = order_details
        self.ui = Ui_ProductBox()
        self.ui.setupUi(self)
        self.parent_class = parent

        self.product_name = order_details.get('product_name')
        self.start = order_details.get('start')
        self.status = order_details.get('status')
        image_path = order_details.get('images')
        self.pixmap = QPixmap(image_path)
        if order_details.get('price'):
            self.price = order_details.get('price')
            self.ui.price_label.setText("Price: " + str(self.price) + " B")
        else:
            self.ui.price_label.setText(" ")
        self.ui.view_product_button.setText("Configure")
        self.ui.product_image_label.setPixmap(self.pixmap)
        self.ui.product_name_label.setText(self.product_name)
        self.ui.sale_date_label.setText("Sale Date: " + self.start.strftime("%Y-%m-%d %H:%M:%S"))
        self.ui.status_label.setText("Status: " + self.status)

        self.ui.view_product_button.clicked.connect(self.to_add_product_page)

    def to_add_product_page(self):
        # Call the method from StoreUI class
        self.parent_class.edit_product_page(self.order_details)

class StoreUI(QMainWindow):
    def __init__(self, stacked_widget,server_host, server_port):
        super(StoreUI, self).__init__()
        self.stacked_widget = stacked_widget
        self.server_host = server_host
        self.server_port = server_port
        self.POST_WIDTH = 230
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.store_stack_widget = self.ui.stackedWidget
        self.store_stack_widget.setCurrentIndex(0)
        self.ui.info_button.clicked.connect(self.to_information_page)
        self.ui.products_button.clicked.connect(self.to_products_page)
        # self.ui.collections_button.clicked.connect(self.to_collections_page)
        self.ui.orders_button.clicked.connect(self.to_orders_page)
        # self.ui.reviews_button.clicked.connect()
        self.new_pic_bytes = None
        self.ui.home_button.clicked.connect(self.to_home_page)
        self.ui.history_button.clicked.connect(self.to_history_page)
        self.ui.wishlist_button.clicked.connect(self.to_wishlist_page)
        self.ui.info_button.clicked.connect(self.to_info_page)

        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: self.update_order_data(self.order_filter))
        self.timer.timeout.connect(lambda: self.update_product_data(self.product_filter))
        self.timer.start(2000)

        # Information page (button)
        self.ui.info_page_edit_button.clicked.connect(lambda: self.select_picture(self.ui.info_page_picture))
        self.ui.info_page_save_button.clicked.connect(self.save_info_page)
        
        #Product page (button)
        self.ui.product_page_add_product_button.clicked.connect(self.to_add_product_page)
        # self.ui.edit_product_page_save_button.clicked.connect(self.update_product_to_database)
    
        #Item page (button)
        self.ui.collection_page_add_collection_button.clicked.connect(self.to_add_item_page)
        self.ui.edit_collection_page_add_product.clicked.connect(self.to_add_product_page)

        self.order_filter = "all"
        self.product_filter = "all"
        #Orders page (button)
        self.ui.order_page_all_button.clicked.connect(lambda: self.update_order_data())
        self.ui.orders_page_unpaid_button.clicked.connect(lambda: self.update_order_data("unpaid"))
        self.ui.orders_page_shipping_button.clicked.connect(lambda: self.update_order_data("shipping"))
        self.ui.orders_page_completed_button.clicked.connect(lambda: self.update_order_data("completed"))
        self.ui.oders_page_cancelled_button.clicked.connect(lambda: self.update_order_data("cancelled"))

        #Productss page(button)
        self.ui.product_page_all_button.clicked.connect(lambda: self.update_product_data())
        self.ui.product_page_live_button.clicked.connect(lambda: self.update_product_data("available"))
        self.ui.product_page_starting_button.clicked.connect(lambda: self.update_product_data("upcoming"))
        self.ui.product_page_completed_button.clicked.connect(lambda: self.update_product_data("sold out"))

    
    def to_home_page(self):
        self.stacked_widget.setCurrentIndex(1) 
    def to_history_page(self):
        self.stacked_widget.setCurrentIndex(5)
    def to_wishlist_page(self):
        self.stacked_widget.setCurrentIndex(6)
    def to_info_page(self):
        self.stacked_widget.setCurrentIndex(3)    
    def to_information_page(self):
        self.store_stack_widget.setCurrentIndex(0)
    def to_products_page(self):
        self.store_stack_widget.setCurrentIndex(1)
        self.product_filter = "all"
    def to_collections_page(self):
        self.store_stack_widget.setCurrentIndex(2)
        self.product_filter = "all"
    def to_orders_page(self):
        self.store_stack_widget.setCurrentIndex(3)
        self.order_filter = "all"
    def to_add_item_page(self):
        self.store_stack_widget.setCurrentIndex(5)

    # def update_product_to_database(self):
        
    
    def to_add_product_page(self):
        self.store_stack_widget.setCurrentIndex(4)
        self.ui.edit_product_page_name_Edit.setText("")
        self.ui.edit_product_page_price_edit.setText("")

        date = datetime.datetime.now()
        qdate_obj = QDate(date.year, date.month, date.day)
        self.ui.edit_product__page_tags_edit.setText("")
        self.ui.edit_product_page_mode_combobox.setCurrentIndex(0) #cf no cc only
        self.ui.edit_product_page_date_edit.setDate(qdate_obj)
        self.ui.edit_product_page_des_edit.setText("")

    def edit_product_page(self, product_detail):
        self.store_stack_widget.setCurrentIndex(4)
        self.ui.edit_product_page_name_Edit.setText(product_detail.get('product_name'))
        self.ui.edit_product_page_price_edit.setText(str(product_detail.get('price')))

        tag_str = ""
        for tag in product_detail.get('tags'):
            tag_str += tag.get('tag_text') + " "

        date = product_detail.get('start')
        qdate_obj = QDate(date.year, date.month, date.day)
        self.ui.edit_product__page_tags_edit.setText(tag_str)
        self.ui.edit_product_page_mode_combobox.setCurrentIndex(0) #cf no cc only
        self.ui.edit_product_page_date_edit.setDate(qdate_obj)
        self.ui.edit_product_page_des_edit.setText(product_detail.get('description'))

        binary_image = product_detail.get('images')
        image_path = QPixmap(binary_image)
        self.ui.edit_product_page_image_label.setPixmap(image_path)
        
    
    def receive_large_data(self, conn):
        total_chunks = pickle.loads(conn.recv(4096))
        received_data = b''
        for _ in range(total_chunks):
            chunk = conn.recv(4096)
            received_data += chunk
            # print(f'chunk {chunk}')
        return pickle.loads(received_data)

            
    def send_large_data(self, connection, data):
        try:
            # Calculate the total number of chunks
            total_chunks = (len(data) + 4095) // 4096
            
            # Send the total number of chunks as the initial message
            connection.sendall(pickle.dumps(total_chunks))
            
            # Send actual data chunks
            for chunk_start in range(0, len(data), 4096):
                chunk_end = min(chunk_start + 4096, len(data))
                connection.sendall(data[chunk_start:chunk_end])
            # print("Data sent successfully.")
        except Exception as e:
            print("Error sending data:", e)

            
    def fetch_check_store_exist(self, user_id, user_name):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            try:
                print("Checking Store exists")
                # print("Step 1: Establishing connection...")
                client_socket.connect((self.server_host, self.server_port))
                # print("Step 2: Sending request...")
                request_data = {'action': 'check_store', 'user_name': user_name["username"]}
                client_socket.sendall(pickle.dumps(request_data))
                # print("Step 3: Receiving response...")
                response_data = self.receive_large_data(client_socket)
                # print("Received response:", response_data)
                # print("Step 4: Unpacking response...")
                if response_data['success']:
                    # print("Check store exists")
                    if response_data['exists']:
                        return self.initial_pages(response_data["store_data"])
                else:
                    print("Failed to check to store:", response_data['message'])
            except Exception as e:
                print("Failed to check to store::", e)
                
    def update_post_image(self, image_label, new_image):
        scaled_pic = new_image.scaled(QSize(self.POST_WIDTH, self.POST_WIDTH), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image_label.setPixmap(scaled_pic)
        
        
    def select_picture(self, image_label):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Picture", "", "Image Files (*.png *.jpg)", options=options)
        if file_name:
            new_pic = QPixmap(file_name)
            self.update_post_image(image_label, new_pic)

    def save_info_page(self):
        # Retrieve current picture from the label if available
        current_pic = self.ui.info_page_picture.pixmap()
        if current_pic:
            # Convert QPixmap to QImage
            current_image = current_pic.toImage()
            # Create a QBuffer to hold the binary data
            buffer = QBuffer()
            buffer.open(QBuffer.ReadWrite)
            # Save the image to the buffer
            current_image.save(buffer, "WEBP")
            # Get the binary data from the buffer
            binary_data = buffer.data()
            buffer.close()
            
        new_info_data ={
            "store_id" : self.store_id,
            "user_name" : self.user_name,
            "store_name" : self.ui.info_page_name_edit.toPlainText(),
            "email" : self.ui.info_page_email_edit.toPlainText(),
            "phone_number" : self.ui.info_page_phone_number_edit.toPlainText(), 
            "description" : self.ui.info_page_description_edit.toPlainText(),
            "picture" : binary_data
        }
        
        # print(new_info_data)
        # print("-----NEW INFORMATION DATA--------")
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            try:
                print("Checking Store exists")
                # print("Step 1: Establishing connection...")
                client_socket.connect((self.server_host, self.server_port))
                # print("Step 2: Sending request...")
                request_data = {'action': 'handle_new_store_info', 'new_store_info': new_info_data}
                # print(f"REQUEST DATA {request_data}")
                self.send_large_data(client_socket, pickle.dumps(request_data))
                #For small data
                # client_socket.sendall(pickle.dumps(request_data))
                # print("Step 3: Receiving response...")
                response_data = self.receive_large_data(client_socket)
                # print("Received response:", response_data)
                # print("Step 4: Unpacking response...")
                if response_data['success']:
                    print(response_data['success'])
                else:
                    print("Failed to save information of store:", response_data['success'])
            except Exception as e:
                print("Failed to save information of store(e):", e)

            
    def initial_pages(self, store_data):
        self.user_name = store_data["store_user_name"]
        self.store_id = store_data["store_id"]
        #Information Page
        self.ui.info_page_name_edit.setText(store_data["store_name"])
        self.ui.info_page_email_edit.setText(store_data["email"])
        self.ui.info_page_phone_number_edit.setText(store_data["phone_number"]) 
        self.ui.info_page_description_edit.setText(store_data["description"])
        
        self.info_page_pic = QPixmap(store_data["picture"])
        self.update_post_image(self.ui.info_page_picture,self.info_page_pic)
        #Product page
        
    
    #orders ui
    def clear_frame(self, frame):
        layout = frame.layout()
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def populate_orders(self, order_details, filter):
        self.order_filter = filter
        self.clear_frame(self.ui.orders_scrollAreaWidgetContents)
        layout = self.ui.orders_scrollAreaWidgetContents.layout()
        for order_detail in order_details:
            # print(f'populating {order_detail}')
            if order_detail.get('order_seller') == self.user_data.get('username'):
                if filter == "all":
                    order = OrderBox(order_detail, self.server_host, self.server_port, self)
                    layout.addWidget(order)
                elif order_detail.get('order_status') == filter:
                    order = OrderBox(order_detail, self.server_host, self.server_port, self)
                    layout.addWidget(order)
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)

    def populate_items(self, product_details, filter):
        self.product_filter = filter
        self.clear_frame(self.ui.collections_scrollAreaWidgetContents)
        self.clear_frame(self.ui.products_crollAreaWidgetContents)
        collection_layout = self.ui.collections_scrollAreaWidgetContents.layout()
        product_layout = self.ui.products_crollAreaWidgetContents.layout()
        # print('helo', product_details)

        for product_detail in product_details:
            # print(f'populating {product_details}')

            if product_detail.get('type') == "collection":
                if product_detail.get('seller') == self.user_data.get('username'):
                    if filter == "all":
                        product = ProductBox(product_detail, self)
                        collection_layout.addWidget(product)
                    elif product_detail.get('status') == filter:
                        product = ProductBox(product_detail, self)
                        collection_layout.addWidget(product)
            elif product_detail.get('type') == "item":
                if product_detail.get('seller') == self.user_data.get('username'):
                    if filter == "all":
                        product = ProductBox(product_detail, self)
                        product_layout.addWidget(product)
                    elif product_detail.get('status') == filter:
                        product = ProductBox(product_detail, self)
                        product_layout.addWidget(product)
                    

            spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
            collection_layout.addItem(spacer)
            spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
            product_layout.addItem(spacer)


    def receive_large_data(self, conn):
            total_chunks = pickle.loads(conn.recv(4096))
            received_data = b''
            for _ in range(total_chunks):
                chunk = conn.recv(4096)
                received_data += chunk
                # print(f'chunk {chunk}')
            return pickle.loads(received_data)

    def get_all_orders(self):
        print('Getting orders from the server')
        retries = 10
        for attempt in range(retries):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                    print("Step 1: Establishing connection...")
                    client_socket.connect((self.server_host, self.server_port))
                    print("Step 2: Sending request...")
                    request_data = {'action': 'get_all_orders', 'user_name' : self.user_data["username"]}
                    client_socket.sendall(pickle.dumps(request_data))
                    print("Step 3: Receiving response...")
                    response = self.receive_large_data(client_socket)
                    # print("Received response:", response)
                    print("Step 4: Unpacking response...")
                    if response.get('success'):
                        print('Success getting all the order')
                        return response.get('order_details')
        
                    else:
                        print("Failed to get all the data:", response.get('message'))
            except socket.error as se:
                print("Socket error:", se)
            except pickle.PickleError as pe:
                print("Error in pickle operation:", pe)
                if attempt < retries - 1: 
                    print("Retrying...")
                    time.sleep(1)
                    continue
            except Exception as e:
                print("ERROR:", e)

    def get_all_items(self):
        print('Getting items from the server')
        retries = 10
        for attempt in range(retries):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                    # print("Step 1: Establishing connection...")
                    client_socket.connect((self.server_host, self.server_port))
                    # print("Step 2: Sending request...")
                    request_data = {'action': 'get_all_items', 'user_name' : self.user_data["username"]}
                    # print(f'sending {request_data}')
                    client_socket.sendall(pickle.dumps(request_data))
                    # print("Step 3: Receiving response...")
                    response = self.receive_large_data(client_socket)
                    # print("Received response:", response)
                    # print("Step 4: Unpacking response...")
                    if response.get('success'):
                        print('Success getting all items')
                        # print(response)
                        return response.get('item_details')
        
                    else:
                        print("Failed to get all the data:", response.get('message'))
            except socket.error as se:
                print("Socket error:", se)
            except pickle.PickleError as pe:
                print("Error in pickle operation:", pe)
                if attempt < retries - 1: 
                    print("Retrying...")
                    # time.sleep(1)
                    continue
            except Exception as e:
                print("ERROR:", e)

    def load_user_data(self, user_id, user_data):
        self.user_id = user_id
        self.user_data = user_data

    def update_order_data(self, filter="all"):
        # try:
        if self.user_data:
            username = self.user_data.get("username")
            if username:
                user_data = self.get_all_orders()

                self.populate_orders(user_data, filter)
                

        # except:
        #     print("\n\nERROR\n\n")

    def update_product_data(self, filter="all"):
        # try:
        if self.user_data:
            username = self.user_data.get("username")
            if username:
                user_data = self.get_all_items()
                if user_data:
                    self.populate_items(user_data, filter)

        # except:
        #     print("\n\nERROR\n\n")
        
class Paying(QDialog):
    def __init__(self, slip_path, order_details, server_host, server_port):
        super(Paying, self).__init__()
        self.server_host = server_host
        self.server_port = server_port
        self.order_id = order_details.get('order_id')
        self.status = order_details.get('order_status')
        self.ui = Ui_confirm()
        self.ui.setupUi(self)
        self.slip_path = slip_path
        self.ui.add_silp_button.clicked.connect(self.confirm_status)
        if slip_path != '':
            self.ui.queue_label.setText("Customer already pay")
            self.ui.queue_label_2.setText("Please recheck the slip carefully")
            self.ui.add_silp_button.setText("Confirm Slip")
            self.ui.qr_label.setPixmap(QPixmap(slip_path))
        else: 
            self.ui.add_silp_button.setText(" ")
            self.ui.queue_label.setText("Customer does not pay yet")
            self.ui.queue_label_2.setText("Waiting for customer to upload the slip")

    def confirm_status(self):
        if self.slip_path != '' and self.status == "unpaid":
            self.update_status(self.order_id, "shipping")
        elif self.slip_path != '' and self.status == "shipping":
            self.update_status(self.order_id, "completed")
    
    def update_status(self, order_id, status):
        try:
            print("\n\n\n")
            print("UPDATE STATUS TO -> " + status)
            print("\n\n\n")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((self.server_host, self.server_port))
                request_data = {'action': 'update_status', 'order_id' : order_id, 'status': status}
                print("SSENT REQEUST DATA")
                client_socket.sendall(pickle.dumps(request_data))
                print("RECEIVE DATA")
                response = self.receive_large_data(client_socket)
                print("Received response:", response)
                if response.get('success'):
                    print('Success saving file path')
                else:
                    print("Failed to get all the data:", response.get('message'))
        except socket.error as se:
            print("Socket error:", se)
        except Exception as e:
            print("ERROR:", e)     
    
    def receive_large_data(self, conn):
            total_chunks = pickle.loads(conn.recv(4096))
            received_data = b''
            for _ in range(total_chunks):
                chunk = conn.recv(4096)
                received_data += chunk
                # print(f'chunk {chunk}')
            return pickle.loads(received_data)

        
 