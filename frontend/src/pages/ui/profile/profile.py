from .profile_ui import Ui_Dialog
from .profile_address_ui import Ui_Dialog as Ui_Dialog_Address
from PySide6.QtWidgets import QDialog
import socket, pickle

class ProfileUI(QDialog):
    def __init__(self, stacked_widget,server_host, server_port, user_id):
        super(ProfileUI, self).__init__()
        self.stacked_widget = stacked_widget
        self.server_host = server_host
        self.server_port = server_port
        self.user_id = user_id
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.address_button.clicked.connect(self.to_addresspage)
        self.ui.info_button.clicked.connect(self.to_infopage)
        self.ui.save_button.clicked.connect(self.save_new_info)
        self.name = self.ui.name_edit
        self.mail = self.ui.mail_edit
        self.phone = self.ui.phonenum_edit
        self.male = self.ui.male_botton
        self.female = self.ui.female_botton
        # self.other = self.ui.others_button
        # self.fetch_user_data()
        
    def to_addresspage(self):
        self.stacked_widget.setCurrentIndex(4)
        print("Clicked to address page from info page")
        
    def to_infopage(self):
        print("Clicked info page from info page")

                
    def save_new_info(self):
        print(f"Name: {self.name.toPlainText()}, Mail: {self.mail.toPlainText()}, Phone: {self.phone.toPlainText()}") 
             
         

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
