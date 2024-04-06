import sys
import os
import socket
import pickle
import traceback
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from .collection_ui import *

current_directory = os.getcwd()
sys.path.append(current_directory)

from frontend.src.pages.ui.common import *

class CollectionUI(QMainWindow):
    def __init__(self, stacked_widget, server_host, server_port):
        QMainWindow.__init__(self, None)
        self.stacked_widget = stacked_widget
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.server_host = server_host
        self.server_port = server_port
        self.details = None
        self.user_id = None
        self.user_date = None

        # nav bar
        button_stylesheet = (
            "QPushButton {"
            "   border-radius: 5px;"
            "   padding: 10px;"
            "   background-color: #fff;"
            "}"
            "QPushButton:hover {"
            "   background-color: #eee;"
            "}"
        )
        self.ui.home_button.setStyleSheet(button_stylesheet)
        self.ui.profile_button.setStyleSheet(button_stylesheet)
        self.ui.wishlist_button.setStyleSheet(button_stylesheet)
        self.ui.history_button.setStyleSheet(button_stylesheet)

        filter_stylesheet = (
            "QPushButton {"
            "   border-radius: 20px;"
            "   background-color: #fff;"
            "}"
            "QPushButton{"
            "   background-color: transparent;"
            "}"
            "QPushButton::icon:hover { color: rgb(255, 231, 204); }"
        )
        self.ui.filter_button.setStyleSheet(filter_stylesheet)

        self.ui.profile_button.clicked.connect(self.to_profile)
        self.ui.history_button.clicked.connect(self.to_history)
        self.ui.wishlist_button.clicked.connect(self.to_wishlist)
        self.ui.home_button.clicked.connect(self.to_home)
        
        self.ui.buy_bt.clicked.connect(self.make_order)
        
    def send_large_data(self, conn, data):
        try:
            # Send metadata or instructions about the data
            if isinstance(data, dict):
                conn.sendall(pickle.dumps(data))
                return

            # Send total number of chunks for large data
            total_chunks = len(data) // 4096 + 1
            conn.sendall(pickle.dumps(total_chunks))

            # Send actual data chunks
            for i in range(0, len(data), 4096):
                chunk = data[i:i+4096]
                print(chunk)
                conn.sendall(chunk)
        except Exception as e:
            print("Error sending data:", e)
        
    def show_item_data(self, item_index):
        if item_index == 0:
            print("old path", self.old_path)
            self.load_user_data(self.details, self.old_path)
        item_details = self.items[item_index]
        print(f'got item details, {item_details.get("product_id")}')

        self.update_name_label(item_details.get('product_name'))
        new_path = self.path.append((item_details.get('product_name'), self.items, item_index))
        self.update_path_label(new_path)
        self.set_images(item_details.get('images'))
        self.update_product_type_label('Item')
        self.populate_tags(item_details.get('tags'))
        self.update_description_label(item_details.get('description'))

        clear_widget(self.ui.horizontalLayout_3)
        self.ui.horizontalLayout_3.addWidget(self.ui.next_item_bt)
        self.ui.horizontalLayout_3.addWidget(self.ui.prev_item_bt)
        
    def update_name_label(self, new_name):
        self.ui.name_label.setText(new_name)
        print("Name label updated:", new_name)

    def update_product_type_label(self, new_product_label):
        self.ui.label_2.setText(new_product_label)
        print("Product type label updated:", new_product_label)
    
    def set_images(self, new_images):
        self.images = []
        for image_data in new_images:
            image = QImage.fromData(image_data)
            self.images.append(image)
        self.set_image(self.images[0])
        print("Images set:", len(self.images))

    def update_path_label(self, new_path):
         # making the path label
        path_font = QFont()
        path_font.setFamily("Manrope")
        path_font.setPointSize(20)
        path_font.setBold(True)

        clear_widget(self.ui.path_widget)
        self.path_label = QLabel(self.ui.path_widget)
        self.ui.path_widget_layout.addWidget(self.path_label)
        self.ui.path_widget_layout.setContentsMargins(0, 0, 0, 0)
        # self.path_label.setText('TESt')
        self.path_label.setGeometry(QRect(60, 110, 591, 61))
        self.path_label.setFont(path_font)
        self.path_label.setStyleSheet("color: #8C237C;\n")
        path_layout = QHBoxLayout(self.path_label)
        self.path_label.setLayout(path_layout)
        path_layout.setAlignment(Qt.AlignLeft)
        path_layout.setSpacing(0)
        print(f'path {new_path}')
        for node in new_path:
                # PathSource(source name, stack, stack_index, collection_ui) returns a Clickable Label
                path_source = PathSource(node[0], node[1], node[2], self).get_path_source()
                path_source.setStyleSheet('color: #8C237C;')
                path_source.setFont(path_font)
                path_layout.addWidget(path_source)
                set_preferred_size(path_source)

                # the > between paths
                if node != new_path[-1]:
                    divider = PathDivider().get_divider()
                    set_preferred_size(divider)
                    divider.setFont(path_font)
                    path_layout.addWidget(divider)
                # self.ui.path_label.setStyleSheet('border: 1px solid black;') #to check box
        # path to current page
        # path_source = PathSource(self.product_name, self.stacked_widget, 1, self).get_path_source()
        # path_source.setFont(path_font)
        # path_layout.addWidget(path_source)
        # set_preferred_size(path_source)
        # print("Path label updated.")

    def load_post_data(self, details, path):
        # getting info from home ui's signal
        # keep items in a list so its just a list of one item for Item obj
        # self.stacked_products.insertWidget(0, self)
        self.old_path = path
        self.details = details
        self.p_type = details.get('product_type')
        self.product = details.get('product')
        self.items = []
        self.items.append(self.product)
        if self.product.get('status') == "available":
            self.status = 'Available'
        elif self.product.get('status') == 'upcoming':
            self.status = 'Upcoming'
        elif self.product.get('status') == 'sold out':
            self.status = 'Sold Out'

        if self.product.get('items'):
            for item in self.product.get('items'):
                self.items.append(item)

        self.product_name = details.get('title')
        print(f'path before', path)
        path.append((self.product_name, self.items, 0))
        self.path = path
        print(self.path)
        self.s_type = details.get('sales_type')
        self.tags = details.get('tags')
        self.start = self.product.get('start')
        self.info = details.get('info')
        self.stock = self.product.get('stock')

        #convert image binary data to usable image
        self.images = []
        for image_data in self.product.get('images'):
            image = QImage.fromData(image_data)
            self.images.append(image)

        #use the first image as cover
        self.set_image(self.images[0])

        #font to be used for info
        info_font = QFont()
        info_font.setFamily("Manrope")
        info_font.setPointSize(13)
        info_font.setBold(True)

        # making the name label
        self.update_product_type_label(self.p_type)
        self.update_name_label(self.product_name)

        # making the path label
        # print("asjfioejsalijijdf", self.path)
        self.update_path_label(self.path)

        # tags frame for this post
        self.ui.tags_frame_widget.setFixedSize(QSize(600, 50))
        self.ui.tags_frame_widget.setLayout(self.ui.tags_frame_layout)
        self.ui.tags_frame_layout.setSpacing(10)
        self.ui.tags_frame.setMinimumSize(QSize(600, 50))
        self.ui.tags_frame.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.populate_tags(self.tags)
        
        # Info Section
        self.ui.label_5.setText("Product Information")
        # self.ui.frame_3.setStyleSheet(f'border:1px solid black;')

        self.ui.mode_label_label.setText("Sales Type:")
        self.ui.mode_label_label.setFont(info_font)

        self.ui.date_label_label.setText("Scheduled For:")
        self.ui.date_label_label.setFont(info_font)

        self.ui.description_label_label.setText("Description:")
        self.ui.description_label_label.setFont(info_font)

        self.ui.status_label_label.setText("Status:")
        self.ui.status_label_label.setFont(info_font)

        self.ui.stock_label_label.setText("In Stock:")
        self.ui.stock_label_label.setFont(info_font)

        info_font.setPointSize(12)
        info_font.setBold(False)
        # self.ui.product_type_label.setText(self.p_type)
        self.ui.product_type_label.setFont(info_font)
        self.update_product_type_label(self.p_type)

        # self.ui.mode_label.setText(self.s_type)
        self.ui.mode_label.setFont(info_font)
        self.update_sales_type(self.s_type)

        # self.ui.date_label.setText(self.start.strftime('%B %d, %y @ %I:%M %p'))
        self.ui.date_label.setFont(info_font)
        self.update_date(self.start)

        # self.ui.description_label.setText(self.info)
        self.ui.description_label.setFont(info_font)
        self.update_description_label(self.info)

        self.ui.status_label.setFont(info_font)
        self.update_status_label(self.status)
        self.ui.status_label.setStyleSheet('color:rgb(137, 153, 211);')

        self.ui.stock_label.setFont(info_font)
        self.update_stock_label(str(self.stock))

        self.update_store_name_label(self.details.get('author_name'))
        author_pic = self.details.get('author_pic')
        self.author_pic = QImage.fromData(author_pic)
        self.update_store_image(self.author_pic)
        self.store_data = self.get_store_data()

        # Buttons
        self.ui.horizontalLayout_3.addWidget(self.ui.add_to_wishlist_bt)
        self.ui.add_to_wishlist_bt.setMaximumSize(QSize(200, 50))
        if self.details.get('status') != 'sold out':
            self.ui.horizontalLayout_3.addWidget(self.ui.buy_bt)
            self.ui.buy_bt.setMaximumSize(QSize(200, 50))
            
        if self.p_type.lower() == 'collection':
            self.ui.horizontalLayout_3.addWidget(self.ui.view_products_bt)

            self.ui.horizontalLayout_3.addWidget(self.ui.go_to_item)
            self.ui.go_to_item.clicked.connect(self.show_item_data(1))
        print("Post data loaded.")
        
    def update_status_label(self, new_status):
        new_status[1].upper()
        self.ui.status_label.setText(new_status)
    
    def update_stock_label(self, stock):
        self.ui.stock_label.setText(stock)

    def receive_large_data(self, conn):
        total_chunks = pickle.loads(conn.recv(4096))
        received_data = b''
        for _ in range(total_chunks):
            chunk = conn.recv(4096)
            received_data += chunk
        return pickle.loads(received_data)
    
    def get_store_data(self):
        print('Getting store data')
        retries = 100
        for attempt in range(retries):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                    client_socket.connect((self.server_host, self.server_port))
                    request_data = {'action': 'get_store', 'store_id': self.details.get('author_id')}
                    client_socket.sendall(pickle.dumps(request_data))
                    response = self.receive_large_data(client_socket)
                    if response.get('success'):
                        store_data = response.get('store_data')
                        self.update_store_data(store_data)
                        return store_data
                    else:
                        print("Failed to get all the data:", response.get('message'))
            except socket.error as se:
                print("Socket error:", se)
            except pickle.PickleError as pe:
                print("Error in pickle operation:", pe)
            except Exception as e:
                print("An unexpected error occurred:", e)
                traceback.print_exc()
                if attempt < retries - 1: 
                    print("Retrying...")
                    continue
    # def __init__(self, order_id, product, buyer, seller, status="unpaid"):        
    def make_order(self):
        print('\n\n\n\n MAKE ORDER \n\n\n\n\n')
        if self.ui.status_label.text() == "Available":
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                try:
                    print("Creating new order")
                    print("Step 1: Establishing connection...")
                    client_socket.connect((self.server_host, self.server_port))
                    print("Step 2: Sending request...")
                    request_data = {'action': 'make_order', 'product' : self.product, 'buyer' : self.user_data['username'], 'seller' : self.ui.store_name_label.text(), "status": "unpaid"}
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
                        print("Creating new order:", response_data['success'])
                except Exception as e:
                    print("Failed to Creating new order(e):", e)
        else: print("STATUS NONONO")
    def update_store_data(self, store_data):
        print('store data', store_data.get('store_id'))
        author_pic = store_data.get('picture')
        author_pic = QImage.fromData(author_pic)
        self.update_store_image(self, author_pic)
        self.update_store_name_label(store_data.get('store_name'))
        self.update_store_description_label(store_data.get('description'))

    def update_store_description(self, store_description):
        self.ui.store_description_label.setText(store_description)

    def update_store_image(self, store_image):
        self.ui.label_9.setPixmap(QPixmap(store_image))

    def update_store_name_label(self, store_name):
        self.ui.store_name_label.setText(store_name)

    def update_sales_type(self, new_s_type):
        self.ui.mode_label.setText(new_s_type)
        print("Sales type label updated:", new_s_type)
    
    def update_date_label(self, new_start):
        if isinstance(new_start, str):
            self.ui.date_label.setText(new_start)
        else:
            new_start_str = new_start.strftime('%B %d, %y @ %I:%M %p')
            self.ui.date_label.setText(new_start_str)
            QTimer.singleShot(1000, lambda: self.update_date(new_start))

    def update_date(self, new_start):
        current_datetime = datetime.now()
        time_difference = new_start - current_datetime
        self.remaining_time = max(0, time_difference.total_seconds())
        days, remainder = divmod(self.remaining_time, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        if self.remaining_time == 0:
            self.ui.date_label.setText("Live Now")
            self.status = "Available"
            self.update_status_label(self.status)
        elif days > 1:
            self.update_date_label(new_start.strftime('%B %d, %y @ %I:%M %p'))
        else:
            self.update_date_label("{:02d}:{:02d}".format(int(hours), int(minutes)))
            QTimer.singleShot(1000, lambda: self.update_date(new_start))


    def update_description_label(self, new_info):
        self.ui.description_label.setText(new_info)
        print("Description label updated:", new_info)

    def populate_tags(self, tags):
        # calculate the total width of all tags plus padding to get how many rows needed
        i = 0
        total_width = 0
        for tag in tags:
            tag_button = BigPostTagButton(tag.get('tag_text'))
            total_width += set_preferred_size(tag_button.get_tag_button()).size().width()
            total_width += (5 * len(self.tags))
        clear_widget(self.ui.tags_frame_widget)
        # if total_width > self.ui.tags_frame.viewport().size().width():
        #     print("Horizontal overflow detected")
        #     print(f'total width: {total_width}\n {self.ui.tags_frame.viewport().size().width()}')
        num_columns = self.ui.tags_frame.viewport().size().width() // 100
        for tag in tags:
            tag_button = BigPostTagButton(tag.get('tag_text'), self.ui.tags_frame_widget)
            row = i // num_columns
            column = i % num_columns
            self.ui.tags_frame_layout.addWidget(set_preferred_size(tag_button.get_tag_button()), row, column, alignment=Qt.AlignTop)
            i += 1
        spacers_needed = num_columns - (len(self.tags) % num_columns)
        for _ in range(spacers_needed):
            row = i // num_columns
            column = i % num_columns
            self.ui.tags_frame_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum), row, column)
            i += 1
        print("Tags populated.")

    def add_info_widget(self, info, layout, font):
        w = QLabel(info)
        w.setFont(font)
        layout.addWidget(set_preferred_size(w, 20, 12))
        return w
    
    def set_image(self, image):
        pic = QPixmap(image)
        scaled_pic = pic.scaled(self.ui.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.image_label.setPixmap(scaled_pic)
        print("Image set.")

    def load_user_data(self, user_id, user_data):
        self.user_id = user_id
        self.user_data = user_data
        print('Received userdata and userid')
    
    def handle_path_click(self, path_source):
        print(f'\n{path_source.get_name()} clicked')
        print(f'{path_source.get_stacked_widget()}')
        print(f'{path_source.get_stacked_index()}\n')
        stacked_widget = path_source.get_stacked_widget()
        self.index = path_source.get_stacked_index()
        if isinstance(stacked_widget, QStackedWidget):
            stacked_widget.setCurrentIndex(self.index)
        elif isinstance(stacked_widget, list):
            print("index", self.index)
            self.show_item_data(self.items[self.index])       

    def to_profile(self):
        self.stacked_widget.setCurrentIndex(3)
        print("Switched to profile page.")
    def to_history(self):
        self.stacked_widget.setCurrentIndex(5)
        print("Switched to history page.")
    def to_wishlist(self):
        self.stacked_widget.setCurrentIndex(6)
        print("Switched to wishlist page.")
    def to_home(self):
        self.stacked_widget.setCurrentIndex(1)
        print("Switched to home page.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    collection_ui = CollectionUI()
    sys.exit(app.exec())
