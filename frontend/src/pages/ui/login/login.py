import sys, os
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from .login_ui import Ui_Dialog
from ..home.home import HomeUI
import socket
import pickle
sys.path.append(r'C:\Users\Miki Ajiki\Desktop\Curate')
from backend import *
class LoginUI(QDialog):
    def __init__(self, stacked_widget):
        super(LoginUI, self).__init__()
        self.stacked_widget = stacked_widget
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(1200, 800)
        self.setWindowTitle("Login Page")
        
        self.ui.password_input.setEchoMode(QLineEdit.Password)
        self.ui.login_btn.clicked.connect(self.login)
        self.ui.register_btn.clicked.connect(self.to_registerpage)
        
        self.server_host = 'localhost'
        self.server_port = 9999
    
    def to_homepage(self):
        self.stacked_widget.setCurrentIndex(1)
    
    def to_registerpage(self):
        self.stacked_widget.setCurrentIndex(2)
        
    def login(self):
        email = self.ui.gmail_input.text()
        password = self.ui.password_input.text()
        
        if not email or not password:
            self.ui.error_txt.setText('Please enter both email and password')
            return
        
        # Create a socket connection to the server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            try:
                client_socket.connect((self.server_host, self.server_port))
                request_data = {'action': 'login', 'email': email, 'password': password}
                client_socket.sendall(pickle.dumps(request_data))
                response = client_socket.recv(4096)
                response_data = pickle.loads(response)
                if response_data.get('success'):
                    # Login successful, proceed to homepage
                    self.stacked_widget.setCurrentIndex(1)
                    print("Login Successful")
                else:
                    # Display error message
                    self.ui.error_txt.setText('Invalid Gmail or Password')
            except Exception as e:
                self.ui.error_txt.setText(str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_ui = LoginUI(None)
    login_ui.show()
    sys.exit(app.exec())
