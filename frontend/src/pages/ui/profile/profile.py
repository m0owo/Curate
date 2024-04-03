from .profile_ui import Ui_Dialog
from .profile_address_ui import Ui_Dialog as Ui_Dialog_Address
from .add_address_ui import Ui_Dialog as Ui_Add_Address
from PySide6.QtWidgets import *
from PySide6.QtCore import QDate, Qt
import socket, pickle
import json, os

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

class ProfileUI(QDialog):
    def __init__(self, stacked_widget,server_host, server_port):
        super(ProfileUI, self).__init__()
        self.stacked_widget = stacked_widget
        self.server_host = server_host
        self.server_port = server_port
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

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
        
    def to_infopage(self):
        print("Clicked info page from info page")
                
    def save_new_info(self):
        print(f"Name: {self.name.toPlainText()}, Mail: {self.mail.toPlainText()}, Phone: {self.phone.toPlainText()}") 
             
        
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
                print("Error saving new information:", e)
         

class ProfileAddressUI(QDialog):
    def __init__(self, stacked_widget):
        super(ProfileAddressUI, self).__init__()
        self.stacked_widget = stacked_widget
        self.ui = Ui_Dialog_Address()
        self.ui.setupUi(self)
        self.ui.home_button.clicked.connect(self.to_home_page)
        self.ui.history_button.clicked.connect(self.to_history_page)
        self.ui.wishlist_button.clicked.connect(self.to_wishlist_page)
        self.ui.info_button.clicked.connect(self.to_info_page)
        self.ui.address_button.clicked.connect(self.to_address_page)
        self.ui.add_address_button.clicked.connect(self.add_address)
    
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
        
    def add_address(self):
        add_address_dialog = AddAddressUI()  # Create an instance of AddAddressUI
        add_address_dialog.exec()
        

class AddAddressUI(QDialog):
    def __init__(self):
        super(AddAddressUI, self).__init__()
        self.ui = Ui_Add_Address()
        self.ui.setupUi(self)
        self.ui.cancel_button.clicked.connect(self.reject)
        
        for province in provinces:
            self.ui.province_combobox.addItem(province['provinceNameEn'])
        
        self.ui.province_combobox.currentIndexChanged.connect(self.handle_province_changed)
        self.ui.district_combobox.currentIndexChanged.connect(self.handle_district_changed)
        self.ui.sub_district_combobox.currentIndexChanged.connect(self.handle_sub_district_changed)
        self.ui.postal_code_combobox.currentIndexChanged.connect(self.handle_postal_code_changed)
        
        
    def handle_province_changed(self, index):
        # Clear existing items in district_combobox
        self.ui.district_combobox.clear()
        # Find districts corresponding to the selected province
        # selected_province = next((p for p in provinces_data if p['provinceNameEn'] == province_name), None)
        # if selected_province:
        #     province_code = selected_province['provinceCode']
        #     districts = [d for d in districts if d['provinceCode'] == province_code]
        #     for district in districts:
        #         self.ui.district_combobox.addItem(district['districtNameEn'])

    def handle_district_changed(self, index):
        # Update sub-district combobox based on selected district
        selected_district = self.district_combobox.currentText()
        # Logic to populate sub-district combobox based on the selected district

    def handle_sub_district_changed(self, index):
        # Update province and district combobox based on selected sub-district
        selected_sub_district = self.sub_district_combobox.currentText()
        # Logic to update province and district combobox based on the selected sub-district

    def handle_postal_code_changed(self, index):
        # Update province, district, and sub-district combobox based on selected postal code
        selected_postal_code = self.postal_code_combobox.currentText()
        # Logic to update province, district, and sub-district combobox based on the selected postal code
