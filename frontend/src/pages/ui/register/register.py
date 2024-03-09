import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from .register_ui import Ui_Dialog

class RegisterUI(QDialog):
    def __init__(self):
        super(RegisterUI, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(1200, 800)
        self.setWindowTitle("Login Page")