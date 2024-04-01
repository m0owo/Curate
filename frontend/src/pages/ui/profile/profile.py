from .profile_ui import Ui_Dialog
from .profile_address_ui import Ui_Dialog as Ui_Dialog_Address
from PySide6.QtWidgets import *
from PySide6.QtCore import QDate, Qt
import socket, pickle

class ProfileUI(QDialog):
    def __init__(self, stacked_widget,server_host, server_port):
        super(ProfileUI, self).__init__()
        self.stacked_widget = stacked_widget
        self.server_host = server_host
        self.server_port = server_port
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.home_button.clicked.connect(self.to_home_page)
        self.ui.history_button.clicked.connect(self.to_history_page)
        self.ui.wishlist_button.clicked.connect(self.to_wishlist_page)
        self.ui.info_button.clicked.connect(self.to_info_page)
        self.ui.address_button.clicked.connect(self.to_address_page)
        
        self.ui.save_button.clicked.connect(self.save_new_info)
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
            elif self.ui.others_botton.setChecked(True):
                sex == "Others"
                
        # Set the birthdate using QDateEdit
        birthdate = self.user_data['birthdate']
        if birthdate:
            year, month, day = birthdate.year, birthdate.month, birthdate.day
            qdate = QDate(year, month, day)
            self.ui.dateEdit.setDate(qdate)
            
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
        self.ui.info_button.clicked.connect(self.to_infopage)
        self.ui.address_button.clicked.connect(self.to_addresspage)

    def to_infopage(self):
        self.stacked_widget.setCurrentIndex(3)
        print("Clicked info page from address page")   
        
    def to_addresspage(self):
        print("Clicked address page from address page")
