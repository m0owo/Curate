import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from .login_ui import Ui_Dialog
from ..home.home import HomeUI

class LoginUI(QDialog):
    def __init__(self, stacked_widget):
        super(LoginUI, self).__init__()
        self.stacked_widget = stacked_widget
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(1200, 800)
        self.setWindowTitle("Login Page")
        
        self.ui.password_input.setEchoMode(QLineEdit.Password)
        self.ui.login_btn.clicked.connect(self.to_homepage)
        self.ui.register_btn.clicked.connect(self.to_registerpage)

    def to_homepage(self):
        self.stacked_widget.setCurrentIndex(1)
    
    def to_registerpage(self):
        self.stacked_widget.setCurrentIndex(2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_ui = LoginUI(None)
    login_ui.show()
    sys.exit(app.exec())