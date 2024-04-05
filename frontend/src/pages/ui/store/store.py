from .s_info_ui import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import socket, pickle
from PySide6.QtGui import *
import io
from PIL import Image
import socket

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
        self.ui.collections_button.clicked.connect(self.to_collections_page)
        self.ui.orders_button.clicked.connect(self.to_orders_page)
        # self.ui.reviews_button.clicked.connect()
        self.new_pic_bytes = None
        self.ui.home_button.clicked.connect(self.to_home_page)
        self.ui.history_button.clicked.connect(self.to_history_page)
        self.ui.wishlist_button.clicked.connect(self.to_wishlist_page)
        self.ui.info_button.clicked.connect(self.to_info_page)

        
        # Information page (button)
        self.ui.info_page_edit_button.clicked.connect(lambda: self.select_picture(self.ui.info_page_picture))
        self.ui.info_page_save_button.clicked.connect(self.save_info_page)
        
        #Product page (button)
        self.ui.product_page_add_product_button.clicked.connect(self.to_add_product_page)
    
        #Item page (button)
        self.ui.collection_page_add_collection_button.clicked.connect(self.to_add_item_page)
        self.ui.edit_collection_page_add_product.clicked.connect(self.to_add_product_page)
    
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
    def to_collections_page(self):
        self.store_stack_widget.setCurrentIndex(2)
    def to_orders_page(self):
        self.store_stack_widget.setCurrentIndex(3)
    def to_add_product_page(self):
        self.store_stack_widget.setCurrentIndex(4)
    def to_add_item_page(self):
        self.store_stack_widget.setCurrentIndex(5)
    
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
            print("Data sent successfully.")
        except Exception as e:
            print("Error sending data:", e)

            
    def fetch_check_store_exist(self, user_id, user_name):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            try:
                print("Checking Store exists")
                print("Step 1: Establishing connection...")
                client_socket.connect((self.server_host, self.server_port))
                print("Step 2: Sending request...")
                request_data = {'action': 'check_store', 'user_name': user_name["username"]}
                client_socket.sendall(pickle.dumps(request_data))
                print("Step 3: Receiving response...")
                response_data = self.receive_large_data(client_socket)
                print("Received response:", response_data)
                print("Step 4: Unpacking response...")
                if response_data['success']:
                    print("Check store exists")
                    if response_data['exists']:
                        return self.initial_pages(response_data["store_data"])
                else:
                    print("Failed to check to store:", response_data['message'])
            except Exception as e:
                print("Failed to check to store::", e)
                
    def update_post_image(self, image_label, new_image):
        scaled_pic = new_image.scaled(QSize(self.POST_WIDTH, self.POST_WIDTH), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image_label.setPixmap(scaled_pic)
        
    # converting binary image data into QImages 
    def convert_image_to_Qimages(self, pictures):
        images = []
        for image_data in pictures:
                image = QImage.fromData(image_data)
                images.append(image) 
        return images[0]
        
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
            # If you need to work with BytesIO, you can convert QByteArray to bytes
            binary_bytes = bytes(binary_data)
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
                print("Step 1: Establishing connection...")
                client_socket.connect((self.server_host, self.server_port))
                print("Step 2: Sending request...")
                request_data = {'action': 'handle_new_store_info', 'new_store_info': new_info_data}
                print(f"REQUEST DATA {request_data}")
                self.send_large_data(client_socket, pickle.dumps(request_data))
                #For small data
                # client_socket.sendall(pickle.dumps(request_data))
                print("Step 3: Receiving response...")
                response_data = self.receive_large_data(client_socket)
                print("Received response:", response_data)
                print("Step 4: Unpacking response...")
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
        
        self.info_page_pic = QPixmap(self.convert_image_to_Qimages(store_data["picture"]))
        self.update_post_image(self.ui.info_page_picture,self.info_page_pic)
        
        #Product page
        
        
        
        
 