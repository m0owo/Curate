import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtWidgets import QWidget
from .history_ui import *
from .historyBox_ui import *
from .paying_ui import Ui_Dialog as Ui_paying
import os
import pickle
import socket
import shutil
from promptpay import qrcode

current_directory = os.getcwd()
sys.path.append(current_directory)
sys.path.append(r'/Users/musicauyeung/Documents/KMITL/Year 2/Curate')
sys.path.append(r'/Users/Miki Ajiki/desktop/Curate')

from frontend.src.pages.ui.common import *

        
class HistoryBox(QFrame):
    def __init__(self, order_details):
        QFrame.__init__(self, None)
        self.ui = Ui_HistoryBox()
        self.ui.setupUi(self)
        self.order_details = order_details
        self.product_name = order_details.get('product_name')
        self.order_id = order_details.get('order_id')
        self.price = order_details.get('price')
        self.order_status = order_details.get('order_status')
        file_path = order_details.get('images')
        self.pixmap = QPixmap(file_path)

        self.ui.product_image_label.setPixmap(self.pixmap)
        self.ui.product_name_label.setText(self.product_name)
        self.ui.order_id_label.setText(str(self.order_id))
        self.ui.price_label.setText(str(self.price) + " B")
        self.ui.status_label.setText("Status: " + self.order_status)
        self.user_id = None
        self.user_data = None

        if self.order_status == "unpaid":
            self.ui.view_order_button.setText("Pay By QR")
            self.ui.view_order_button.clicked.connect(self.show_payment_popup)
        elif self.order_status == "shipping":
            self.ui.view_order_button.setText("Confirm Shipping")
            self.ui.view_order_button.clicked.connect(self.confirm_shipping)
        elif self.order_status == "completed":
            self.ui.view_order_button.setText("Completed")
        elif self.order_status == "cancelled":
            self.ui.view_order_button.setText("Cancelled")

    def confirm_shipping(self):
        self.order_status = "completed"
        self.ui.view_order_button.setText("Completed")
        
        
    def show_payment_popup(self):
        # self.ui.view_order_button.setText("Shipping")
        # self.order_status = "shipping"
        payment_popup = Paying(self.order_details)
        payment_popup.exec_()


class HistoryUI(QMainWindow):
    def __init__(self, stacked_widget, server_host, server_port):
        QMainWindow.__init__(self, None)
        self.stacked_widget = stacked_widget
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.server_host = server_host
        self.server_port = server_port
        self.filter = "all"

        # nav bar
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
        self.ui.wishlist_button.clicked.connect(self.to_wishlist_page)
        self.ui.profile_button.clicked.connect(self.to_profile_page)

        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: self.update_history_data(self.filter))
        self.timer.start(10000)

        self.ui.all.clicked.connect(lambda: self.update_history_data())
        self.ui.to_pay.clicked.connect(lambda: self.update_history_data("unpaid"))
        self.ui.to_be_delivered.clicked.connect(lambda: self.update_history_data("shipping"))
        self.ui.completed.clicked.connect(lambda: self.update_history_data("completed"))
        self.ui.cancelled.clicked.connect(lambda: self.update_history_data("cancelled"))
        self.user_id = None
        self.user_data = None
        
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
        self.filter = filter
        self.clear_frame(self.ui.scrollAreaWidgetContents)
        layout = self.ui.scrollAreaWidgetContents.layout()
        if order_details:
            for order_detail in order_details:
                # print(f'populating {order_detail}')
                if order_detail.get('order_buyer') == self.user_data.get('username'):
                    if filter == "all":
                        order = HistoryBox(order_detail)
                        layout.addWidget(order)
                    elif order_detail.get('order_status') == filter:
                        order = HistoryBox(order_detail)
                        layout.addWidget(order)
        else: ("No user order details for populate order")
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

    def get_all_orders(self, filter="all"):
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
                        print('Success getting all the data')
                        return response.get('order_details')
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
                    
    def update_history_data(self, filter="all"):
        try:
            username = self.user_data.get("username")
            if username:
                user_data = self.get_all_orders()
                if user_data:
                    self.populate_orders(user_data, filter)
                else:
                    print("Fail")
        except Exception as e:
                print("Error update history data:", e)
        
class Paying(QDialog):
    def __init__(self, order_details):
        super(Paying, self).__init__()
        self.ui = Ui_paying()
        self.ui.setupUi(self)  
        self.order_details = order_details
        self.price = order_details.get('price')
        self.order_id = order_details.get('order_id')
        # Generate QR code
        self.generate_qr_code("0943422221", self.price)
        
        save_path = f"slip-{self.order_id}.jpg"
        filepath = f"./{self.order_id}.png"
        
        if os.path.exists(save_path):
            self.ui.qr_label.setPixmap(QPixmap(save_path))
            self.ui.add_silp_button.hide()
            self.ui.queue_label_2.setText("Thanks you, plase wait for seller to confirm")
        else:
            self.ui.qr_label.setPixmap(QPixmap(filepath))
        
        self.ui.add_silp_button.clicked.connect(self.upload_slip)
        
    def generate_qr_code(self, id, amount):
        payload = qrcode.generate_payload(id, amount)
        print("payload of %s: %s" % (id, payload))
        filepath = f"./{self.order_id}.png"
        if filepath:
            qrcode.to_file(payload, filepath)
    def change_ui(self):
        self.ui.add_silp_button.hide()
        self.ui.queue_label_2.setText("Thanks you, plase wait for seller to confirm")       
    def upload_slip(self):
        options = QFileDialog.Options()
        picture_path, _ = QFileDialog.getOpenFileName(self, "Select Picture", "", "Image Files (*.png *.jpg *.jpeg)", options=options)
        if picture_path:
            # Modify this path to your desired save location
            save_path = f"slip-{self.order_id}.jpg"
            # Copy the selected picture to the save path
            shutil.copy(picture_path, save_path)
            self.ui.qr_label.setPixmap(QPixmap(save_path))
            self.change_ui()
            print("Picture saved successfully.")
            
        
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    history_ui = HistoryUI()
    history_ui.show()
    sys.exit(app.exec())
