import sys, os
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from .login_ui import Ui_Dialog
import socket
import pickle
import zlib
current_directory = os.getcwd()
print("Current directory:", current_directory)
sys.path.append(current_directory)
from backend import *

class LoginUI(QDialog, QObject):
    login_successful = Signal(int, dict, dict)
    def __init__(self, stacked_widget, server_host, server_port):
        super(LoginUI, self).__init__()
        self.stacked_widget = stacked_widget
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(1200, 800)
        self.setWindowTitle("Login Page")
        
        self.ui.password_input.setEchoMode(QLineEdit.Password)
        self.ui.login_btn.clicked.connect(self.login)
        self.ui.register_btn.clicked.connect(self.to_registerpage)
        
        self.server_host = server_host
        self.server_port = server_port
    def to_homepage(self):
        self.stacked_widget.setCurrentIndex(1)
    
    def to_registerpage(self):
        self.stacked_widget.setCurrentIndex(2)
        
    def send_data_in_chunks(self, socket, data):
        try:
            serialized_data = pickle.dumps(data)
            total_size = len(serialized_data)
            socket.sendall(total_size.to_bytes(4, byteorder='big'))  # Send total size of data
            sent_size = 0
            while sent_size < total_size:
                chunk_size = min(4096, total_size - sent_size)  # Send data in chunks of 4096 bytes
                socket.sendall(serialized_data[sent_size:sent_size + chunk_size])
                sent_size += chunk_size
            print("Data sent successfully")
        except Exception as e:
            print("Error sending data:", e)

    def receive_data_in_chunks(self, socket):
        try:
            total_size_bytes = socket.recv(4)  # Receive total size of data
            total_size = int.from_bytes(total_size_bytes, byteorder='big')
            print("Total size of data to receive:", total_size)  # Debug print
            received_data = b''
            while len(received_data) < total_size:
                remaining_bytes = total_size - len(received_data)
                chunk_size = min(4096, remaining_bytes)
                print("Remaining bytes:", remaining_bytes)  # Debug print
                print("Chunk size to receive:", chunk_size)  # Debug print
                chunk = socket.recv(chunk_size)  # Receive data in chunks of 4096 bytes
                if not chunk:
                    break
                received_data += chunk
                print("Received chunk of data, total size received:", len(received_data))  # Debug print
            data = pickle.loads(received_data)
            print("Data received successfully")
            return data
        except Exception as e:
            print("Error receiving data:", e)
            return None

        
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
                serialized_data = pickle.dumps(request_data)
                client_socket.sendall(serialized_data)

                # Receiving data
                response_data = client_socket.recv(4096)  # Adjust buffer size as needed
                response_dict = pickle.loads(response_data)
                if response_dict and response_dict.get('success'):
                        # Login successful, proceed to homepage
                    user_id = response_dict.get('user_id')
                    user_data = response_dict.get('user_data')  # Extract user data
                    # Decompress posts_data using zlib
                    compressed_posts_data = response_dict.get('posts_data')
                    if compressed_posts_data:
                        posts_data = zlib.decompress(compressed_posts_data)
                    else:
                        posts_data = None
                    self.login_successful.emit(user_id, user_data, posts_data)  # Pass user data and posts data to signal
                    self.stacked_widget.setCurrentIndex(1)
                    print("Login Successful")
                else:
                    # Display error message
                    self.ui.error_txt.setText('Invalid Gmail or Password')
            except Exception as e:
                self.ui.error_txt.setText(str(e))
                print(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_ui = LoginUI(None)
    login_ui.show()
    sys.exit(app.exec())
