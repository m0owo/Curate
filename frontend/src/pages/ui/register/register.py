import sys, socket, pickle
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from .register_ui import Ui_Dialog

class RegisterUI(QDialog):
    def __init__(self, server_host, server_port):
        super(RegisterUI, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(1200, 800)
        self.setWindowTitle("Login Page")
        self.ui.register_button.clicked.connect(self.create_account)
        self.server_host = server_host
        self.server_port = server_port
    
    def create_account(self):
        email = self.ui.gmail_input.text()
        username = self.ui.username_input.text()
        password = self.ui.password_input.text()
        reconfirm_pass = self.ui.reconfirm_input.text()
        account_type = None
        if self.ui.buyer_button.isChecked():
            account_type = 'customer'
        elif self.ui.seller_button.isChecked():
            account_type = 'seller'
        else:
            self.ui.noti_label.setText('Please select account type')

        if not email or not password or not reconfirm_pass or not username:
            self.ui.noti_label.setText('Please fill in all required fields')
            return
        if password != reconfirm_pass:
            self.ui.noti_label.setText('Passwords do not match')
            print(password.text())
            print(reconfirm_pass.text())
            return
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            try:
                client_socket.connect((self.server_host, self.server_port))
                request_data = {
                    'action': 'register',
                    'username' : username,
                    'account_type': account_type,
                    'email': email,
                    'password': password,
                }
                client_socket.sendall(pickle.dumps(request_data))
                response = client_socket.recv(4096)
                response_data = pickle.loads(response)
                if response_data.get('success'):
                    self.ui.noti_label.setText('Registration successful')
                    print(f"Create account successful {email}, {username} as {account_type} " )
                else:
                    print(response_data.get('message', 'Registration failed'))
                    self.ui.noti_label.setText(response_data.get('message', 'Registration failed'))
            except Exception as e:
                self.ui.noti_label.setText(str(e))
                print(e)