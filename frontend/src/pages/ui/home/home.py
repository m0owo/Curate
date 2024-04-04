import sys
import os
import pickle
import socket
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap, QImage
from .home_ui import *
from datetime import datetime, timedelta
import time

current_directory = os.getcwd()
sys.path.append(current_directory)
# sys.path.append(r'/Users/musicauyeung/Documents/KMITL/Year 2/Curate')
sys.path.append(r'/Users/Miki Ajiki/desktop/Curate')

from frontend.src.pages.ui.common import *

# from .icons_rc import *
# from .logo_rc import *
# from .post_images_rc import *

class Post():
    def __init__(self, details, container, home_ui):
        self.POST_WIDTH = 230
        self.post = ClickablePost(container, details, home_ui)

        # making the clickable frame for the post
        post_layout = QVBoxLayout()
        post_layout.setAlignment(Qt.AlignCenter)
        post_layout.setContentsMargins(0, 0, 0, 0)
        post_layout.setSpacing(0)
        self.post.setLayout(post_layout)
        self.post.setMinimumSize(QSize(self.POST_WIDTH, 300))
        self.post.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        # self.post.setStyleSheet("border: 1px solid black;") #for showing the boxes
        self.post.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        card_shadow = QGraphicsDropShadowEffect(self.post)
        card_shadow.setBlurRadius(10)
        card_shadow.setXOffset(1)
        card_shadow.setYOffset(1)
        self.post.setGraphicsEffect(card_shadow)

        # check the post details exists
        if details:
            self.id = details.get('post_id')
            self.author = details.get('post_author')
            self.product = details.get('product')
            self.info = details.get('info')
            self.title = details.get('title')
            self.created = details.get('created')
            self.modified = details.get('modified')
            self.p_type = details.get('product_type')
            self.tags = details.get('tags') #list of tags
            self.s_type = details.get('sales_type')
            self.start = self.product.get('start')
            self.status = details.get('status')

            #if collection: price is tuple(min, max), otherwise its just price string
            if self.p_type.lower() == 'collection':
                price_range = self.product.get('price_range')
                if price_range[0] != price_range[1]:
                    self.price = price_range
                    self.price_str = f'฿{str(self.price[0])} - ฿{str(self.price[1])}'
                else:
                    self.price = f'฿{price_range[0]}'
            elif self.p_type.lower() == 'item':
                self.price = self.product.get('price')
                self.price_str = f'฿{str(self.price)}'

            # converting binary image data into QImages
            self.images = []
            for image_data in self.product.get('images'):
                image = QImage.fromData(image_data)
                self.images.append(image)
            
            self.container = container #the post frame

            self.draw_post_image()
            self.draw_post_info()

    def update_post_image(self, new_image):
        scaled_pic = new_image.scaled(QSize(self.POST_WIDTH, self.POST_WIDTH), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.post_image.setPixmap(scaled_pic)

    def draw_post_image(self):
        #post image
        self.post_image = QLabel(self.post)
        self.post_image.setFixedSize(QSize(self.POST_WIDTH, self.POST_WIDTH))
        self.post_image.setStyleSheet("QLabel { background-color: transparent; }")
        self.post.layout().addWidget(self.post_image, alignment=Qt.AlignTop | Qt.AlignCenter)

        # pic = QPixmap(u":/post_images/IMG_7109.jpg") #test image
        # post image is the first image from the post product
        pic = QPixmap(self.images[0])
        self.update_post_image(pic)
        return pic
        
    def update_post_title(self, new_title):
        self.post_title.setText(new_title)
        return self.post_title
    
    def update_status_countdown(self, new_start_date):
        new_countdown = CountdownWidget(new_start_date)
        return new_countdown
    
    def update_product_type(self, new_p_type):
        new_product_type = ProductTypeTagButton(new_p_type, self.post_tags_widget).get_tag_button()
        return new_product_type
    
    def update_sales_type(self, new_s_type):
        new_sales_type = SaleTypeTagButton(new_s_type, self.post_tags_widget).get_tag_button()
        self.sales_type = new_sales_type
        return self.sales_type
    
    def update_price(self, new_price):
        self.price_label.setText(new_price)

    def draw_post_info(self):
        # post info is a widget for all the information below the images
        self.post_info = QWidget(self.post)
        post_info_layout = QVBoxLayout()
        post_info_layout.setSpacing(10)
        if not self.post_info:
            print('jasofj')
        self.post_info.setLayout(post_info_layout)
        self.post_info.setMinimumSize(QSize(200, 100))
        self.post.layout().addWidget(self.post_info)

        # post title
        self.post_title = QLabel(self.post_info)
        self.post_title.setMinimumSize(QSize(200, 16))
        self.post_title.setStyleSheet(u"QLabel {font: 700 16pt \"Manrope\";}")
        self.post_title.setWordWrap(True)
        self.post_title.setAlignment(Qt.AlignLeft)
        post_info_layout.addWidget(self.post_title, alignment=Qt.AlignCenter)
        self.update_post_title(self.title)
        
        info_font = QFont()
        info_font.setFamilies([u"Manrope"])
        info_font.setPointSize(10)
        info_font.setBold(True)

        label_font = QFont()
        label_font.setFamilies([u"Manrope"])
        label_font.setPointSize(11)

        # self info tag widgets
        self.post_tags_widget = QWidget()
        self.post_tags_widget.setMinimumSize(QSize(200, 40))
        post_info_layout.addWidget(self.post_tags_widget)
        post_tags_layout = QVBoxLayout(self.post_tags_widget)
        post_tags_layout.setContentsMargins(0, 0, 0, 0)
        post_tags_layout.setSpacing(5)

        # product type widget
        self.product_type_widget = QWidget()
        product_type_layout = QHBoxLayout(self.product_type_widget)
        product_type_layout.setAlignment(Qt.AlignLeft)
        product_type_layout.setContentsMargins(0, 0, 0, 0)
        post_tags_layout.addWidget(self.product_type_widget)

        # sales type widget
        self.sales_type_widget = QWidget()
        sales_type_layout = QHBoxLayout(self.sales_type_widget)
        sales_type_layout.setAlignment(Qt.AlignLeft)
        sales_type_layout.setContentsMargins(0, 0, 0, 0)
        post_tags_layout.addWidget(self.sales_type_widget)
        
        # status tag widget
        self.status_widget = QWidget()
        status_layout = QHBoxLayout(self.status_widget)
        status_layout.setContentsMargins(0, 0, 0, 0)
        status_layout.setAlignment(Qt.AlignLeft)
        post_tags_layout.addWidget(self.status_widget)

        # status
        self.status_label = QLabel('Scheduled For:')
        self.status_label.setFont(label_font)
        self.status_countdown = self.update_status_countdown(self.start)
        status_layout.addWidget(self.status_label)
        status_layout.addWidget(self.status_countdown)

        # product type
        self.product_type_label = QLabel('Product Type:')
        self.product_type_label.setFont(label_font)
        self.product_type = self.update_product_type(self.p_type)
        self.product_type.setFont(info_font)
        product_type_layout.addWidget(self.product_type_label)
        product_type_layout.addWidget(self.product_type)

        # sales type
        self.sales_type_label = QLabel('Sales Type:')
        self.sales_type_label.setFont(label_font)
        self.sales_type = self.update_sales_type(self.s_type)
        self.sales_type.setFont(info_font)
        sales_type_layout.addWidget(self.sales_type_label)
        sales_type_layout.addWidget(self.sales_type)

        # post details widget
        self.post_details_widget = QWidget()
        post_info_layout.addWidget(self.post_details_widget)
        post_details_layout = QHBoxLayout(self.post_details_widget)
        post_details_layout.setContentsMargins(0, 0, 0, 0)
        post_details_layout.setSpacing(10)

        # price
        self.price_label = QLabel()
        self.price_label.setStyleSheet("font:500 16pt Manrope;")
        self.price_label.setAlignment(Qt.AlignLeft)
        self.update_price(self.price_str)
        post_details_layout.addWidget(self.price_label)
            
        # self.created_date = QLabel()
        # self.created_date.setText(f'date created: {self.created.strftime("%Y-%m-%d %H:%M:%S")}')
        # self.created_date.setAlignment(Qt.AlignCenter)
        # post_details_layout.addWidget(self.created_date)

        # seller profile?
    def get_post(self):
        return self.post
    def get_status(self):
        return self.status
    def update_status(self):
        cur_time = datetime.now()
        if status != 'timeout':
            if self.start <= cur_time:
                status = 'live'
            elif self.start > cur_time:
                status = 'upcoming'
    def countdown_status(self, target_datetime):
        while True:
            current_datetime = datetime.now()
            remaining_time = max(target_datetime - current_datetime, timedelta(0))
            # print(remaining_time)
            if remaining_time == timedelta(0):
                self.update_status()
                break
    def on_post_clicked(self):
        print("Post clicked!")
        
class HomeUI(QMainWindow):
    post_clicked = Signal(object, list)
    def __init__(self, stacked_widget, server_host, server_port):
        QMainWindow.__init__(self, None)
        self.stacked_widget = stacked_widget
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.server_host = server_host
        self.server_port = server_port

        # nav bar
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(10)
        shadow.setXOffset(1)
        shadow.setYOffset(1)
        self.ui.search_frame.setGraphicsEffect(shadow)
        shadow2 = QGraphicsDropShadowEffect(self)
        shadow2.setBlurRadius(10)
        shadow2.setXOffset(1)
        shadow2.setYOffset(1)
        self.ui.page_label.setGraphicsEffect(shadow2)
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

        self.ui.profile_button.clicked.connect(self.to_profile)
        self.ui.history_button.clicked.connect(self.to_history)
        self.ui.wishlist_button.clicked.connect(self.to_wishlist)
        # self.ui.home_button.clicked.connect(self.to_home)

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

        # clearing tags frame
        clear_frame(self.ui.tags_frame)

        # drawing tags
        self.get_pop_tags()
        
        # drawing posts
        self.get_all_posts()

    def handle_post_click(self, details):
        # sender information is for the path to product and the stackedwidget and stackedwidget index
        # page > collection > item
        sender = ('Home', self.stacked_widget, 1)
        self.post_clicked.connect(self.to_collection) 
        
        # emits the signal with the product details and the sender info
        self.post_clicked.emit(details, [sender])

    def populate_posts(self, post_details):
        #clear the scroll area
        clear_widget(self.ui.scrollAreaWidgetContents)
        self.ui.scrollAreaWidgetContents.setMinimumSize(0, 0)
        self.ui.gridLayout.setSpacing(20)
        post_widgets = []
        i = 0
        spacers_needed = 0 
        for post_detail in post_details:
            # print(f'WEE WOO WEE WOOO WEE WOO {post_detail}')
            post = Post(post_detail, self.ui.scrollAreaWidgetContents, self)
            post_widget = post.get_post()
            post_widgets.append(post_widget)

            row = i // 4
            column = i % 4
            spacers_needed = max(spacers_needed, 4 - column)
            self.ui.gridLayout.addWidget(post_widget, row, column)
            self.ui.gridLayout.setAlignment(post_widget, Qt.AlignTop | Qt.AlignLeft)
            i += 1
        for _ in range(spacers_needed):
            spacer = Spacer().get_spacer()
            self.ui.gridLayout.addWidget(spacer)
        self.ui.scrollAreaWidgetContents.adjustSize()
        return post_widgets
    
        
    def receive_large_data(self, conn):
        total_chunks = pickle.loads(conn.recv(4096))
        received_data = b''
        for _ in range(total_chunks):
            chunk = conn.recv(4096)
            received_data += chunk
            # print(f'chunk {chunk}')
        return pickle.loads(received_data)
    
    def get_all_posts(self):
        print('Getting all posts from the server')
        retries = 100
        for attempt in range(retries):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                    print("Step 1: Establishing connection...")
                    client_socket.connect((self.server_host, self.server_port))
                    print("Step 2: Sending request...")
                    request_data = {'action': 'get_all_posts'}
                    client_socket.sendall(pickle.dumps(request_data))
                    print("Step 3: Receiving response...")
                    response = self.receive_large_data(client_socket)
                    # print("Received response:", response)
                    print("Step 4: Unpacking response...")
                    if response.get('success'):
                        print('Success getting all the data')
                        post_details = response.get('post_details')
                        self.populate_posts(post_details)
                        break 
                    else:
                        print("Failed to get all the data:", response.get('message'))
            except socket.error as se:
                print("Socket error:", se)
            except pickle.PickleError as pe:
                print("Error in pickle operation:", pe)
            except Exception as e:
                print("An unexpected error occurred:", e)
                if attempt < retries - 1: 
                    print("Retrying...")
                    time.sleep(1)
                    continue

    def get_pop_tags(self, user_id = None):
        #get the most popular tags first if no user_id
        pop_tags = {"Crochet", "Y2K", "Summer Outfit", "Bam Yang Gang", "Acubi"}
        self.populate_tags(pop_tags)

    def populate_tags(self, pop_tags):
        print("Populating tags...")
        print("Pop tags:", pop_tags)
        for pop_tag in pop_tags:
            print("Adding tag:", pop_tag)
            TagButton(pop_tag, self.ui.tags_frame)
        print("Tags populated successfully.")
    
    def load_user_data(self, user_id, user_data):
        self.user_id = user_id
        self.user_data = user_data
        # print(f'User ID: {self.user_id}\nUser Data: {self.user_data}')
        self.ui.name_label.setText(f"Welcome, {self.user_data['username']}")

    def to_profile(self):
        self.stacked_widget.setCurrentIndex(3)

    def to_history(self):
        self.stacked_widget.setCurrentIndex(5)

    def to_wishlist(self):
        self.stacked_widget.setCurrentIndex(6)

    def to_collection(self):
        self.stacked_widget.setCurrentIndex(7)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    home_ui = HomeUI()
    home_ui.show()
    sys.exit(app.exec())
