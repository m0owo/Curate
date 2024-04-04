import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from .history_ui import *
from .historyBox_ui import *
import os
import pickle
import socket
import zlib, base64
import time

class HistoryBox(QFrame):
    def __init__(self, order_details):
        QFrame.__init__(self, None)
        self.ui = Ui_HistoryBox()
        self.ui.setupUi(self)

        self.product_name = order_details.get('product_name')
        self.order_id = order_details.get('order_id')
        self.price = order_details.get('price')
        self.order_status = order_details.get('order_status')

        self.ui.product_name_label.setText(self.product_name)
        self.ui.order_id_label.setText(str(self.order_id))
        self.ui.price_label.setText(str(self.price) + " B")
        self.ui.status_label.setText("Status: " + self.order_status)


class HistoryUI(QMainWindow):
    def __init__(self, stacked_widget, server_host, server_port):
        QMainWindow.__init__(self, None)
        self.stacked_widget = stacked_widget
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.server_host = server_host
        self.server_port = server_port

        self.ui.home_button.clicked.connect(self.to_home_page)
        self.ui.wishlist_button.clicked.connect(self.to_wishlist_page)
        self.ui.profile_button.clicked.connect(self.to_profile_page)

        self.ui.all.clicked.connect(lambda: self.get_all_orders("all"))
        self.ui.to_pay.clicked.connect(lambda: self.get_all_orders("unpaid"))
        self.ui.to_be_delivered.clicked.connect(lambda: self.get_all_orders("shipping"))
        self.ui.completed.clicked.connect(lambda: self.get_all_orders("completed"))
        self.ui.cancelled.clicked.connect(lambda: self.get_all_orders("cancelled"))


        self.get_all_orders("all")

    def to_home_page(self):
        self.stacked_widget.setCurrentIndex(1)
    def to_profile_page(self):
        self.stacked_widget.setCurrentIndex(3)
    def to_wishlist_page(self):
        self.stacked_widget.setCurrentIndex(6)

    def clear_frame(self, frame):
        layout = frame.layout()
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def populate_orders(self, order_details, filter):
        self.clear_frame(self.ui.scrollAreaWidgetContents)
        layout = self.ui.scrollAreaWidgetContents.layout()
        for order_detail in order_details:
            # print(f'populating {order_detail}')
            if filter == "all":
                order = HistoryBox(order_detail)
                layout.addWidget(order)
            elif order_detail.get('order_status') == filter:
                order = HistoryBox(order_detail)
                layout.addWidget(order)
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)


    def receive_large_data(self, conn):
            total_chunks = pickle.loads(conn.recv(4096))
            received_data = b''
            for _ in range(total_chunks):
                chunk = conn.recv(4096)
                received_data += chunk
                # print(f'chunk {chunk}')
            return pickle.loads(received_data)

    def get_all_orders(self, filter):
        print('Getting orders from the server')
        retries = 10
        for attempt in range(retries):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                    print("Step 1: Establishing connection...")
                    client_socket.connect((self.server_host, self.server_port))
                    print("Step 2: Sending request...")
                    request_data = {'action': 'get_all_orders'}
                    client_socket.sendall(pickle.dumps(request_data))
                    print("Step 3: Receiving response...")
                    response = self.receive_large_data(client_socket)
                    # print("Received response:", response)
                    print("Step 4: Unpacking response...")
                    if response.get('success'):
                        print('Success getting all the data')
                        order_details = response.get('order_details')
                        self.populate_orders(order_details, filter)
                        break 
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

    def load_user_data(self, user_id, user_data):
        self.user_id = user_id
        self.user_data = user_data
        print(f'User ID: {self.user_id}\nUser Data: {self.user_data}')
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    history_ui = HistoryUI()
    history_ui.show()
    sys.exit(app.exec())