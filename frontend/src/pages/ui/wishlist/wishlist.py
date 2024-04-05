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
        binary_image = product_details.get('images')[0]
        image = QImage.fromData(binary_image)
        self.pixmap = QPixmap.fromImage(image)

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
            products = self.user_data.get('wishlist')
            for product_detail in products:
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

    def load_user_data(self, user_id, user_data):
        self.user_id = user_id
        self.user_data = user_data



if __name__ == "__main__":
    app = QApplication(sys.argv)
    wishlist_ui = WishlistUI()
    wishlist_ui.show()
    sys.exit(app.exec())
