from .profile_ui import Ui_Dialog
from PySide6.QtWidgets import QDialog

class ProfileUI(QDialog):
    def __init__(self,stacked_widget):
        super(ProfileUI, self).__init__()
        self.stacked_widget = stacked_widget
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.address_button.clicked.connect(self.to_addresspage)
        
    def to_addresspage():
        self.stacked_widget.setCurrentIndex(4)            

class ProfileAddressUI(QDialog):
    def __init__(self,stacked_widget):
        super(ProfileAddressUI, self).__init__()
        self.stacked_widget = stacked_widget
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.info_button.clicked.connect(self.to_infopage)

    def to_infopage():
        self.stacked_widget.setCurrentIndex(3)     