from .profile_ui import Ui_Dialog
from .profile_address_ui import Ui_Dialog as Ui_Dialog_Address
from .add_address_ui import Ui_Dialog as Ui_Add_Address
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import socket, pickle
import json, os
from PySide6.QtGui import *
import traceback

# Get the directory of the current script (profile.py)
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the provinces.json file
provinces_file_path = os.path.join(current_directory, "provinces.json")
districts_file_path = os.path.join(current_directory, "districts.json")
sub_districts_file_path = os.path.join(current_directory, "subdistricts.json")

# Load JSON data from files
with open(provinces_file_path, 'r', encoding='utf-8') as f:
    provinces = json.load(f)

with open(districts_file_path, 'r', encoding='utf-8') as f:
    districts = json.load(f)

with open(sub_districts_file_path, 'r', encoding='utf-8') as f:
    sub_districts = json.load(f)
    
def clear_frame(frame):
        for widget in frame.findChildren(QPushButton):
            widget.deleteLater()

def clear_widget(widget):
    for i in reversed(range(widget.layout().count())):
        widget.layout().itemAt(i).widget().setParent(None)
        
def clear_layout(layout):
    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()
        if widget is not None:
            widget.deleteLater()
class Post():
    def __init__(self, details, container):
        if details:
            self.name = details.get('name')
            self.phone_number = details.get('phone_number')
            self.details = details.get('details')
            self.sub_district = details.get('sub_district')
            self.district = details.get('district')
            self.province = details.get('province')
            self.postal_code = details.get('postal')
            self.container = container
            self.container.setStyleSheet(u"border: None;")

            info_text = f"{self.name} {self.phone_number}"
            self.address = f"{self.details} {self.sub_district} {self.district} {self.province} {self.postal_code}"
            
            # Create a main widget to hold the info and address_label
            self.main_widget = QWidget()
            self.main_widget.setStyleSheet(u"border: 1px solid black;")
            main_layout = QVBoxLayout(self.main_widget)
            main_layout.setAlignment(Qt.AlignTop)

            # name and phone number
            self.info = QLabel(info_text)
            self.info.setStyleSheet(u"QLabel {font: 700 11pt \"Manrope\";border: None;}")
            self.info.setWordWrap(True)
            self.info.setAlignment(Qt.AlignLeft)
            main_layout.addWidget(self.info)

            self.address_label = QLabel(self.address)
            self.address_label.setStyleSheet(u"QLabel {font: 9pt \"Manrope\"; border: None;}")
            self.address_label.setWordWrap(True)
            self.address_label.setAlignment(Qt.AlignLeft)
            main_layout.addWidget(self.address_label)
            
            # Set fixed size for the main widget
            self.main_widget.setFixedSize(550, 90)
            
            # Add spacer to push the widget to the top if container layout exists
            if container.layout():
                main_layout.addStretch(1)
        
            # Add the main widget to the container
            if container.layout() is None:
                container.setLayout(QVBoxLayout())
            container.layout().insertWidget(0, self.main_widget)
    def get_name(self):
        return self.name
    def get_post(self):
        return self.main_widget

    
class ProfileUI(QDialog):
    def __init__(self, stacked_widget,server_host, server_port):
        super(ProfileUI, self).__init__()
        self.stacked_widget = stacked_widget
        self.server_host = server_host
        self.server_port = server_port
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

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
        
        self.ui.home_button.clicked.connect(self.to_home_page)
        self.ui.history_button.clicked.connect(self.to_history_page)
        self.ui.wishlist_button.clicked.connect(self.to_wishlist_page)
        self.ui.info_button.clicked.connect(self.to_info_page)
        self.ui.address_button.clicked.connect(self.to_address_page)
        self.ui.address_button_2.clicked.connect(self.to_store_page)
        
        
        self.ui.save_button.clicked.connect(self.save_new_info)
        self.name = self.ui.name_edit
        self.mail = self.ui.mail_edit
        self.phone = self.ui.phonenum_edit
        self.male = self.ui.male_button
        self.female = self.ui.female_button
        # self.other = self.ui.others_button
        
        
    def to_home_page(self):
        self.stacked_widget.setCurrentIndex(1) 
    def to_history_page(self):
        self.stacked_widget.setCurrentIndex(5)
    def to_wishlist_page(self):
        self.stacked_widget.setCurrentIndex(6)
    def to_info_page(self):
        self.stacked_widget.setCurrentIndex(3)
    def to_address_page(self):
        self.stacked_widget.setCurrentIndex(4)
        print("Clicked to address page from info page")
    def to_store_page(self):
        self.stacked_widget.setCurrentIndex(8)
        
    def to_infopage(self):
        print("Clicked info page from info page")
                
    def save_new_info(self):
        print(f"Name: {self.name.toPlainText()}, Mail: {self.mail.toPlainText()}, Phone: {self.phone.toPlainText()}") 
        
    def receive_large_data(self, conn):
        total_chunks = pickle.loads(conn.recv(4096))
        received_data = b''
        for _ in range(total_chunks):
            chunk = conn.recv(4096)
            received_data += chunk
            # print(f'chunk {chunk}')
        return pickle.loads(received_data)

    
    def fetch_check_store_exist(self, user_id, user_name):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            try:
                
                # print("Checking Store exists")
                # print("Step 1: Establishing connection...")
                client_socket.connect((self.server_host, self.server_port))
                # print("Step 2: Sending request...")
                request_data = {'action': 'check_store', 'user_name': user_name["username"]}
                client_socket.sendall(pickle.dumps(request_data))
                print("Step 3: Receiving response...")
                response_data = self.receive_large_data(client_socket)
                # print("Received response:", response_data)
                # print("Step 4: Unpacking response...")
                if response_data['success']:
                    print("Check store exists")
                    if response_data['exists']:
                        print("Bro change my name alr")
                        self.ui.address_button_2.setText("Manage Shop")
                else:
                    print("Failed to check to store:", response_data['message'])
            except Exception as e:
                print("Failed to check to store::", e)
                
    def load_user_data(self, user_id, user_data):
        self.user_id = user_id
        self.user_data = user_data
        # Set user data to corresponding UI elements
        self.ui.name_edit.setPlainText(self.user_data['username'])
        self.ui.mail_edit.setPlainText(self.user_data['email'])
        self.ui.phonenum_edit.setPlainText(self.user_data['phone_number'])
        
        # Set the sex using radio buttons
        sex = self.user_data['sex']
        if sex:
            if self.ui.male_button.setChecked(True):
                sex == "Male"
            elif self.ui.female_button.setChecked(True):
                sex == "Female"
            elif self.ui.others_button.setChecked(True):
                sex == "Others"
                
        # Set the birthdate using QDateEdit
        birthdate = self.user_data['birthdate']
        if birthdate:
            year, month, day = birthdate.year, birthdate.month, birthdate.day
            qdate = QDate(year, month, day)
            self.ui.date_edit.setDate(qdate)
            
            
    def save_new_info(self):
        if self.user_data is None:
            print("No user data available to save.")
            return

        new_info = {
            'username': self.ui.name_edit.toPlainText(),
            'email': self.ui.mail_edit.toPlainText(),
            'phone_number': self.ui.phonenum_edit.toPlainText(),
            'sex': 'Male' if self.ui.male_botton.checkStateSet() == Qt.Checked else
                   'Female' if self.ui.female_botton.checkStateSet() == Qt.Checked else
                   'Others' if self.ui.others_botton.checkStateSet() == Qt.Checked else None,
            'birthdate': self.ui.dateEdit.date().toString(Qt.ISODate)
        }
        print(new_info)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            try:
                client_socket.connect((self.server_host, self.server_port))
                request_data = {'action': 'save_new_info', 'new_info': new_info}
                client_socket.sendall(pickle.dumps(request_data))
                response = client_socket.recv(4096)
                response_data = pickle.loads(response)
                if response_data['success']:
                    print("New information saved successfully")
                else:
                    print("Failed to save new information:", response_data['message'])
            except Exception as e:
                print("Error save_new_info:", e)
         

class ProfileAddressUI(QDialog):
    def __init__(self, stacked_widget, server_host, server_port):
        super(ProfileAddressUI, self).__init__()
        self.stacked_widget = stacked_widget
        self.server_host = server_host
        self.server_port = server_port
        self.ui = Ui_Dialog_Address()
        self.ui.setupUi(self)
        self.ui.home_button.clicked.connect(self.to_home_page)
        self.ui.history_button.clicked.connect(self.to_history_page)
        self.ui.wishlist_button.clicked.connect(self.to_wishlist_page)
        self.ui.info_button.clicked.connect(self.to_info_page)
        self.ui.address_button.clicked.connect(self.to_address_page)
        self.ui.add_address_button.clicked.connect(self.add_address)
        self.ui.create_shop_button.clicked.connect(self.to_store_page)
        self.user_id = None
        self.user_data = None
        
        # Create a QTimer object for periodic updates
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_address_data)
        self.timer.start(2000)  # 2 seconds interval (adjust as needed)
    
    def to_home_page(self):
        self.stacked_widget.setCurrentIndex(1) 
    def to_history_page(self):
        self.stacked_widget.setCurrentIndex(5)
    def to_wishlist_page(self):
        self.stacked_widget.setCurrentIndex(6)
    def to_info_page(self):
        self.stacked_widget.setCurrentIndex(3)
    def to_address_page(self):
        self.stacked_widget.setCurrentIndex(4)
    def to_store_page(self):
        self.stacked_widget.setCurrentIndex(8)
    
    def load_user_data(self, user_id, user_data):
        self.user_id = user_id
        self.user_data = user_data
        self.populate_address_widgets(self.user_data["addresses"])
        
    def populate_address_widgets(self, addresses):
        layout = self.ui.verticalLayout_2
        clear_layout(layout)
        self.ui.scrollAreaWidgetContents.setMinimumSize(QSize(550, 420))
        num_empty_layouts = max(0, 4 - len(addresses))
        layout.setSpacing(100)
        # Iterate through addresses and create post widgets
        for post_detail in addresses:
            # print(f'WEE WOO WEE WOOO WEE WOO {post_detail}')
            post = Post(post_detail, self.ui.scrollAreaWidgetContents)
            post_widget = post.get_post()
            layout.addWidget(post_widget)

        # Fill empty layouts
        for _ in range(num_empty_layouts):
            empty_widget = QWidget()
            empty_widget.setStyleSheet("border: None;")
            layout.addWidget(empty_widget)

        # Adjust the size of the scroll area widget contents
        self.ui.scrollAreaWidgetContents.adjustSize()
    
    def add_address(self):
        add_address_dialog = AddAddressUI(self.server_host, self.server_port, self.user_data)
        add_address_dialog.exec_()
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
                            
    def update_address_data(self):
        print("Updating address data...")
        if self.user_data:
            username = self.user_data.get("username")
            if username:
                user_data = self.fetch_user_data(username)
                if user_data:
                    self.populate_address_widgets(user_data.get("addresses"))
                    print("Address data updated successfully")
                else:
                    print("Failed to fetch updated user data")
        # else:
        #     print("cannot update address data, no user data")
        

class AddAddressUI(QDialog):
    def __init__(self, server_host, server_port, user_data):
        super(AddAddressUI, self).__init__()
        self.ui = Ui_Add_Address()
        self.server_host = server_host
        self.server_port = server_port
        self.user_data = user_data
        self.ui.setupUi(self)
        self.ui.cancel_button.clicked.connect(self.reject)
        self.selected_district_code = None
        
        for province in provinces:
            self.ui.province_combobox.addItem(province['provinceNameEn'])
            
        for district in districts:
            self.ui.district_combobox.addItem(district['districtNameEn'])
            
        for sub_district in sub_districts:
            self.ui.sub_district_combobox.addItem(sub_district['subdistrictNameEn'])
        
        self.ui.province_combobox.currentIndexChanged.connect(self.handle_province_changed)
        self.ui.district_combobox.currentIndexChanged.connect(self.handle_district_changed)
        self.ui.sub_district_combobox.currentIndexChanged.connect(self.handle_sub_district_changed)
        
        self.ui.save_button.clicked.connect(self.save_address_db)
        
        self.load_user_data()
        
    def load_user_data(self):
        print("load user data from the create address")
        
        self.ui.name_edit.clear()
        self.ui.phone_number_edit.clear()
        self.ui.name_edit.setText(self.user_data['username'])
        self.ui.phone_number_edit.setText(self.user_data['phone_number'])
        
    def save_address_db(self):
        new_info = {
            'name': self.ui.name_edit.text(),
            'phone': self.ui.phone_number_edit.text(),
            'province': self.ui.province_combobox.currentText(),
            'district': self.ui.district_combobox.currentText(),
            'sub_district': self.ui.sub_district_combobox.currentText(),
            'postal_code' : self.ui.postal_code_combobox.currentText(),
            'details' : self.ui.details_textedit.toPlainText()
        }
        print(new_info)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            try:
                client_socket.connect((self.server_host, self.server_port))
                request_data = {'action': 'save_new_address', 'new_info': new_info, 'username' : self.user_data["username"]}
                client_socket.sendall(pickle.dumps(request_data))
                response = client_socket.recv(4096)
                response_data = pickle.loads(response)
                if response_data['success']:
                    print("New information saved successfully")
                    self.accept()
                else:
                    print("Failed to save new information:", response_data['message'])
            except Exception as e:
                print("save_address_db", e)
                
    def handle_province_changed(self, index):
        # Clear existing items in district_combobox
        self.ui.district_combobox.clear()
        self.ui.sub_district_combobox.clear()
        self.ui.postal_code_combobox.clear()
        
        selected_province_name = self.ui.province_combobox.currentText()
        
        selected_province_code = None
        for province in provinces:
            if province['provinceNameEn'] == selected_province_name:
                selected_province_code = province['provinceCode']
                break
        
        # Filter districts based on the selected province
        for district in districts:
            if district['provinceCode'] == selected_province_code:
                self.ui.district_combobox.addItem(district['districtNameEn'])
                self.ui.postal_code_combobox.addItem(str(district['provinceCode']))
        
        # Filter sub-districts based on the selected province and district (if applicable)
        for sub_district in sub_districts:
            if sub_district['provinceCode'] == selected_province_code:
                self.ui.sub_district_combobox.addItem(sub_district['subdistrictNameEn'])
                self.ui.postal_code_combobox.addItem(str(sub_district['subdistrictCode']))
        
                

    def handle_district_changed(self, index):
        # Clear existing items in sub_district_combobox
        self.ui.sub_district_combobox.clear()
        self.ui.postal_code_combobox.clear()

        # Get the selected province and district
        selected_province_name = self.ui.province_combobox.currentText()
        selected_district_name = self.ui.district_combobox.currentText()

        # Find the province code for the selected province
        selected_province_code = None
        for province in provinces:
            if province['provinceNameEn'] == selected_province_name:
                selected_province_code = province['provinceCode']
                break

        # Find the district code for the selected district
        for district in districts:
            if district['districtNameEn'] == selected_district_name and district['provinceCode'] == selected_province_code:
                self.selected_district_code = district['districtCode']
                break

        # Filter sub-districts based on the selected district code
        for sub_district in sub_districts:
            if sub_district['districtCode'] == self.selected_district_code:
                self.ui.sub_district_combobox.addItem(sub_district['subdistrictNameEn'])
                self.ui.postal_code_combobox.addItem(str(sub_district['postalCode']))


    def handle_sub_district_changed(self, index):
        self.ui.postal_code_combobox.clear()
        
        selected_sub_district_name = self.ui.sub_district_combobox.currentText()
        
        # Find the postal code for the selected sub-district
        selected_sub_district_postal_code = None
        for sub_district in sub_districts:
            if sub_district['subdistrictNameEn'] == selected_sub_district_name:
                # Check if the district codes match to handle districts with the same name
                if sub_district['districtCode'] == self.selected_district_code:
                    selected_sub_district_postal_code = sub_district['postalCode']
                    break
        
        # Update postal code combobox with the postal code of the selected sub-district
        if selected_sub_district_postal_code is not None:
            self.ui.postal_code_combobox.addItem(str(selected_sub_district_postal_code))
        
