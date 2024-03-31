import socket
import pickle
from database import *


def handle_login(data):
    email = data.get('email')
    password = data.get('password')

    # Retrieve user from the database based on email
    accounts = root.accounts
    for account_id, account in accounts.items():
        if isinstance(account, Admin) or isinstance(account, Customer) or isinstance(account, Seller):
            if account.get_email() == email and account.get_password() == password:
                print(f"ID: {account_id} or {account.get_email()} Account_name {account.username}")
                return {'success': True, 'message': 'Login successful', 'user_id': account.id, 'user_data': account.serialize()}
    
    return {'success': False, 'message': 'Invalid credentials'}

        
def handle_registration(data):
    account_type = data.get('account_type')
    email = data.get('email')
    password = data.get('password')
    username = data.get('username')
    sex = data.get('sex')
    address = data.get('address')

    try:
        root = connection.root
        accounts = root.accounts

        # Find the next available ID
        max_id = max(accounts.keys(), default=0)
        new_id = max_id + 1

        # Create new account based on account_type
        if account_type == 'customer':
            new_account = Customer(email, password)
            new_account.sex = sex
            new_account.address = address
        elif account_type == 'seller':
            new_account = Seller(email, password)
            new_account.address = address
        else:
            return {'success': False, 'message': 'Invalid account type'}

        accounts[new_id] = new_account
        new_account.username = username
        transaction.commit()
        print("Account created successfully")
        return {'success': True, 'message': 'Account created successfully'}
    except Exception as e:
        return {'success': False, 'message': str(e)}

def get_user_data(data):
    user_id = data.get('user_id')
    accounts = root.accounts
    if user_id in accounts:
        user = accounts[user_id]
        #Add attributes as needed
        user_data = {
            'name': user.username,  
            'mail': user.mail,
            'phone': user.phone,
            'address' : user.address,
            'follower' : user.follower,
            'following' : user.following,
            'sex' : user.sex
        }
        return {'success': True, 'user_data': user_data}
    else:
        return {'success': False, 'message': 'User not found'}

def handle_request(conn):
    try:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            data_dict = pickle.loads(data)
            action = data_dict.get('action')
            if action == 'login':
                response = handle_login(data_dict)
            elif action == 'register':
                response = handle_registration(data_dict)
            else:
                response = {'success': False, 'message': 'Invalid action'}
            conn.sendall(pickle.dumps(response))
    except Exception as e:
        print("Error handling request:", e)
    finally:
        conn.close()


def start_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print("Server listening on", host, port)
        try:
            while True:
                conn, addr = server_socket.accept()
                print("Connected to", addr)
                handle_request(conn)
        except KeyboardInterrupt:
            print("Server shutting down.")

if __name__ == "__main__":
    start_server('localhost', 8888)  # Change host and port as needed
