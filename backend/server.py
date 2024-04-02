import socket
import pickle
from database import *
import zlib

def handle_login(data):
    email = data.get('email')
    password = data.get('password')

    # Retrieve user from the database based on email
    accounts = root.accounts
    posts = root.posts
    for account_id, account in accounts.items():
        if isinstance(account, Admin) or isinstance(account, Customer) or isinstance(account, Seller) or isinstance(account, Account):
            if account.get_email() == email and account.get_password() == password:
                print(f"ID: {account.get_id()} or {account.get_email()} Account_name {account.get_username()}")
                user_id = account_id
                user_data = account.serialize()
                break  # Assuming you found the user, exit the loop
    else:
        # If the loop completes without finding a matching user, return False
        return {'success': False, 'message': 'Invalid credentials'}

    # Search for the post in the database
    for post_id, post in posts.items():
        post_data = post.serialize()  # Serialize post data
        break
    else:
        # If the loop completes without finding a post authored by the user, return False
        return {'success': False, 'message': 'No post found for this user'}

    # Compress the serialized post_data using zlib
    compressed_post_data = zlib.compress(pickle.dumps(post_data))

    # Return success along with combined data
    return {'success': True, 'message': 'Login successful', 'user_id': user_id, 'user_data': user_data, 'posts_data': compressed_post_data}

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

def handle_request(conn):
    try:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            print("Received data from client:", data)  # Debug print
            data_dict = pickle.loads(data)
            print("Received data dictionary:", data_dict)  # Debug print
            action = data_dict.get('action')
            print("Received action:", action)  # Debug print
            if action == 'login':
                response = handle_login(data_dict)
            elif action == 'register':
                response = handle_registration(data_dict)
            else:
                response = {'success': False, 'message': 'Invalid action'}
            conn.sendall(pickle.dumps(response))
            print("Sent response to client:", response)  # Debug print
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
