import sys, socket, pickle
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from .register_ui import Ui_Dialog
from email.message import EmailMessage
import time, ssl, smtplib

def send_confirmation_email(receiver_email, username):
    sender_email = 'officialcurate@gmail.com'  # Your email address
    sender_password = 'nwme bjlz flms yben'  # Your email password

    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Registration Confirmation'

    body = f'Dear {username},\n\nThank you for registering with our platform.\n\nBest regards,\nCurate'
    msg.set_content(body)
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.sendmail(sender_email, receiver_email, msg.as_string())

class RegisterUI(QDialog):
    def __init__(self, widget, server_host, server_port):
        super(RegisterUI, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(1200, 800)
        self.setWindowTitle("Login Page")
        self.ui.register_button.clicked.connect(self.create_account)
        self.server_host = server_host
        self.server_port = server_port
        self.stacked_widget = widget
    
    def create_account(self):
        email = self.ui.gmail_input.text()
        username = self.ui.username_input.text()
        password = self.ui.password_input.text()
        reconfirm_pass = self.ui.reconfirm_input.text()
        account_type = None
        # if self.ui.buyer_button.isChecked():
        #     account_type = 'customer'
        # elif self.ui.seller_button.isChecked():
        #     account_type = 'seller'
        # else:
        #     self.ui.noti_label.setText('Please select account type')

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
                    'password': str(password),
                }
                client_socket.sendall(pickle.dumps(request_data))
                response = client_socket.recv(4096)
                response_data = pickle.loads(response)
                if response_data.get('success'):
                    self.ui.noti_label.setText('Registration successful')
                    print(f"Create account successful {email}, {username} as {account_type} " )
                    if send_confirmation_email(email, username):
                        print("Confirmation email sent successfully")
                    else:
                        print("Failed to send confirmation email") 
                    time.sleep(3)
                    self.stacked_widget.setCurrentIndex(0)
                else:
                    print(response_data.get('message', 'Registration failed'))
                    self.ui.noti_label.setText(response_data.get('message', 'Registration failed'))
            except Exception as e:
                self.ui.noti_label.setText(str(e))
                print(e)