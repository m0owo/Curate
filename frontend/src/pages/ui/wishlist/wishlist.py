import sys
import datetime
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from .wishlist_ui import *
from .wishlist_box import Ui_WishlistBox
import os
import pickle
import socket
import zlib, base64
import time

class WishlistBox(QFrame):
    def __init__(self, product_details):
        QFrame.__init__(self, None)
        self.ui = Ui_WishlistBox()
        self.ui.setupUi(self)

        self.product_name = product_details.get('product_name')
        self.start_date = product_details.get('start')
        self.shop_name = product_details.get('seller')
        self.status = product_details.get('status')
        file_path = product_details.get('images')
        self.pixmap = QPixmap(file_path)

        self.ui.wl_product_image_label.setPixmap(self.pixmap)
        self.ui.wl_product_name_label.setText(self.product_name)
        self.ui.wl_shop_name_label.setText(self.shop_name)
        self.ui.wl_status_label.setText(self.status)
        self.ui.wl_sale_date_label.setText("Sale Date: " + self.start_date.strftime("%Y-%m-%d %H:%M:%S"))

class WishlistUI(QMainWindow):
    def __init__(self, stacked_widget, server_host, server_port):
        QMainWindow.__init__(self, None)
        self.stacked_widget = stacked_widget
        self.server_host = server_host
        self.server_port = server_port
        self.user_id = None
        self.user_data = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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

        self.ui.home_button.clicked.connect(self.to_home_page)
        self.ui.history_button.clicked.connect(self.to_history_page)
        self.ui.profile_button.clicked.connect(self.to_profile_page)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.populate_wishlist)
        self.timer.start(2000)

    def to_home_page(self):
        self.stacked_widget.setCurrentIndex(1)
    def to_profile_page(self):
        self.stacked_widget.setCurrentIndex(3)
    def to_history_page(self):
        self.stacked_widget.setCurrentIndex(5)

    def clear_frame(self, frame):
        layout = frame.layout()
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def populate_wishlist(self):
        try:
            self.clear_frame(self.ui.scrollAreaWidgetContents)
            layout = self.ui.scrollAreaWidgetContents.layout()
            userdata = self.fetch_user_data(self.user_data.get('username'))
            wishlists = userdata.get('wishlist')
            for product_detail in wishlists:
                product = WishlistBox(product_detail)
                layout.addWidget(product)
            spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
            layout.addItem(spacer)
        except:
            pass

    def receive_large_data(self, conn):
            total_chunks = pickle.loads(conn.recv(4096))
            received_data = b''
            for _ in range(total_chunks):
                chunk = conn.recv(4096)
                received_data += chunk
                # print(f'chunk {chunk}')
            return pickle.loads(received_data)
        
    def fetch_user_data(self, username):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            try:
                client_socket.connect((self.server_host, self.server_port))
                request_data = {'action': 'get_user_data', 'username': username}
                client_socket.sendall(pickle.dumps(request_data))
                # response = client_socket.recv(4096)
                response_data = self.receive_large_data(client_socket)
                # response_data = pickle.loads(response)
                if response_data['success']:
                    print("Get new user data done!")
                    return response_data['user_data']
                else:
                    print("Failed to save new information:", response_data['message'])
            except Exception as e:
                print("Error fetch_user_data:", e)
                
    def load_user_data(self, user_id, user_data):
        self.user_id = user_id
        self.user_data = user_data

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wishlist_ui = WishlistUI()
    wishlist_ui.show()
    sys.exit(app.exec())
