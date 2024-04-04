import socket
import pickle
from database import *

def handle_login(data):
    email = data.get('email')
    password = data.get('password')

    # Retrieve user from the database based on email
    accounts = root.accounts
    for account_id, account in accounts.items():
        # if isinstance(account, Admin) or isinstance(account, Customer) or isinstance(account, Seller) or isinstance(account, Account):
        if isinstance(account, Account):
            if account.get_email() == email and account.get_password() == password:
                print(f"ID: {account.get_id()} or {account.get_email()} Account_name {account.get_username()}")
                return {'success': True, 'message': 'Login successful', 'user_id': account.get_id(), 'user_data': account.serialize()}
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
        # if account_type == 'customer':
        #     new_account = Customer(email, password)
        #     new_account.sex = sex
        #     new_account.address = address
        # elif account_type == 'seller':
        #     new_account = Seller(email, password)
        #     new_account.address = address
        # else:
        #     return {'success': False, 'message': 'Invalid account type'}
        
        new_account = Account(email, password)
        new_account.sex = sex
        new_account.address = address

        accounts[new_id] = new_account
        new_account.username = username
        transaction.commit()
        print("Account created successfully")
        return {'success': True, 'message': 'Account created successfully'}
    except Exception as e:
        return {'success': False, 'message': str(e)}

def get_user_data(data):
    user_name = data.get('username')
    accounts = root.accounts
    if user_name in accounts:
        user_data = accounts[user_name].serialize()
        #Add attributes as needed
        return {'success': True, 'user_data': user_data}
    else:
        return {'success': False, 'message': 'User not found'}

def send_large_data(conn, data):
    CHUNK_SIZE = 4096
    serialized_data = pickle.dumps(data)
    total_chunks = (len(serialized_data) + CHUNK_SIZE - 1) // CHUNK_SIZE 
    conn.sendall(pickle.dumps(total_chunks))
    for i in range(total_chunks):
        start_index = i * CHUNK_SIZE
        end_index = min((i + 1) * CHUNK_SIZE, len(serialized_data))
        chunk = serialized_data[start_index:end_index]
        conn.sendall(chunk)

def get_all_posts():
    print("getting all posts server oo ee")
    try:
        post_details = root.posts
        posts_data = [post.serialize() for post in post_details.values()]
        print(f'posts data {posts_data}\n\n')
        return {'success': True, 'post_details': posts_data}
    except Exception as e:
        print(e)
        return {'success': False, 'message': "Failed to return post details"}
    
def get_all_orders():
    print("getting orders")
    try:
        order_details = root.orders
        orders_data = [order.serialize() for order in order_details.values()]
        print(f'order data {orders_data}\n\n')
        return {'success': True, 'order_details': orders_data}
    except Exception as e:
        print(e)
        return {'success': False, 'message': "Failed to return order details"}
    
def handle_save_new_info(data_dict):
    try:
        new_info = data_dict.get('new_info')
        
        birthdate_str = new_info.get('birthdate')
        birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d').date()
        account = root.accounts[new_info.get('username')]
        if account:
            # Update the account information with the new data
            account.phone_number = new_info.get('phone_number', account.phone_number)
            account.sex = new_info.get('sex', account.sex)
            account.birthdate = birthdate
            account.address = new_info.get('address', account.address)

            transaction.commit()
            
            return {'success': True, 'message': 'New information saved successfully'}
        else:
            return {'success': False, 'message': 'Account not found'}
    except Exception as e:
        return {'success': False, 'message': str(e)}

def handle_new_address(data_dict):
    try:
        new_info = data_dict.get('new_info')
        username = data_dict.get('username')
        
        account = root.accounts[username]
        if account:
            new_address = Address(new_info["name"], new_info["phone"], new_info["province"], new_info["district"], 
                                  new_info["sub_district"], new_info["postal_code"], new_info["details"])
            account.addresses.append(new_address)

            transaction.commit()
            return {'success': True, 'message': 'New address saved successfully'}
        else:
            return {'success': False, 'message': 'Account not found'}
    except Exception as e:
        return {'success': False, 'message': str(e)}
        
def handle_request(conn):
    try:
        print("Handling request...")
        while True:
            data = conn.recv(4096)
            if not data:
                print("No data received from client.")
                break
            print("Received data from client:", data)

            data_dict = pickle.loads(data)
            print("Received dictionary:", data_dict)
            action = data_dict.get('action')
            print("Received action:", action)
            
            if action == 'login':
                response = handle_login(data_dict)
            elif action == 'register':
                response = handle_registration(data_dict)
            elif action == 'save_new_info':
                response = handle_save_new_info(data_dict)
            elif action == 'get_all_posts':
                print("Calling get_all_posts()")
                response = get_all_posts()
                send_large_data(conn, response)
            elif action == 'get_all_orders':
                print("Calling get_all_orders()")
                response = get_all_orders()
                send_large_data(conn, response)
            elif action == 'save_new_address':
                response = handle_new_address(data_dict)
            elif action == "get_user_data":
                response = get_user_data(data_dict)
            else:
                print("Invalid action")
                response = {'success': False, 'message': 'Invalid action'}
            
            print("Sending response to client:", response)
            conn.sendall(pickle.dumps(response))
            conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    except Exception as e:
        print("Error handling request:", e)

    finally:
        print("Closing connection.")
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
