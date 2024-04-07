from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import socket
import threading
import pickle
import traceback
from thefuzz import fuzz, process
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

def generate_id(type):
    while str(uuid.uuid4()) in getattr(root, type, []):
        pass
    return str(uuid.uuid4())

def handle_registration(data):
    account_type = data.get('account_type')
    email = data.get('email')
    password = data.get('password')
    username = data.get('username')
    sex = data.get('sex')
    try:
        root = connection.root
        accounts = root.accounts
        new_account = Account(generate_id('accounts'), email, password, username, sex)
        accounts[username] = new_account
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
        return {'success': True, 'message': 'Get account successfully', 'user_data': user_data}
    else:
        return {'success': False, 'message': 'User not found'}
    
def check_store(data):
    user_name = data.get("user_name")
    print("Check whether create a store yet")
    stores = root.stores
    for key in stores:
        if stores[key].store_user_name == user_name:
            return {'success' : True, 'exists' : True, "store_data" : stores[key].serialize()}
        else: return {'success' : True, 'exists' : False}
    return {'success': False, 'exists': False}

        
def send_large_data(conn, data):
    CHUNK_SIZE = 4096
    serialized_data = pickle.dumps(data)
    total_chunks = (len(serialized_data) + CHUNK_SIZE - 1) // CHUNK_SIZE 
    print('total chunks', total_chunks)
    conn.sendall(pickle.dumps(total_chunks))
    for i in range(total_chunks):
        start_index = i * CHUNK_SIZE
        end_index = min((i + 1) * CHUNK_SIZE, len(serialized_data))
        chunk = serialized_data[start_index:end_index]
        conn.sendall(chunk)

def receive_large_data(conn, max_streaming_line=4096):
    try:
        # Receive initial metadata or instructions
        initial_message = pickle.loads(conn.recv(max_streaming_line))
        
        # If the initial message is a dictionary, return it directly
        if isinstance(initial_message, dict):
            return initial_message
        
        # Check if the initial message contains the total number of chunks
        if isinstance(initial_message, int):
            total_chunks = initial_message
            received_data = b""
            chunks_received = 0
            # Receive actual data chunks
            while chunks_received < total_chunks:
                chunk = conn.recv(4096)
                if not chunk:  # Break the loop if no data is received
                    break
                chunks_received += 1
                received_data += chunk
                
            return pickle.loads(received_data)
        
        # Add return statement to make sure the function returns
        return None
    
    except Exception as e:
        print("Error receiving data:", e)
        return None


def get_all_posts():
    print("getting all posts server oo ee")
    try:
        post_details = root.posts
        posts_data = [post.serialize() for post in post_details.values()]
        # print(f'posts data {posts_data}\n\n')
        return {'success': True, 'message' : "return post details valid", 'post_details': posts_data}
    except Exception as e:
        print(e)
        return {'success': False, 'message': "Failed to return post details"}

def get_all_items(data):
    print("getting items")
    print(data)
    try:
        username = data.get("user_name")
        product_details = root.products
        new_product_details = []
        for product_detail in product_details:
            # print(product_details[product_detail].seller)
            if product_details[product_detail].seller == username:
                new_product_details.append(product_details[product_detail])

        # print(new_product_details)
        # products_data = [product.serialize() for product in new_product_details]
        products_data = []
        for product in new_product_details:
            product_data = product.serialize()
            type = ""
            if isinstance(product, Collection):
                type = "collection"
            elif isinstance(product, Item):
                type = "item"
            product_data.update({'type': type})
            products_data.append(product_data)

        # print(f'order data {products_data}\n\n')
        return {'success': True, 'item_details': products_data}
    except Exception as e:
        print(e)
        return {'success': False, 'message': "Failed to return item details"}
def get_all_posts():
    print("getting all posts server oo ee")
    try:
        post_details = root.posts
        posts_data = [post.serialize() for post in post_details.values()]
        # print(f'posts data {posts_data}\n\n')
        return {'success': True, 'message' : "return post details valid", 'post_details': posts_data}
    except Exception as e:
        print(e)
        return {'success': False, 'message': "Failed to return post details"}   
def get_all_orders(data):
    print("getting orders")
    try:
        username = data.get("user_name")
        order_details = root.orders
        # new_order_details = []
        # for order_detail in order_details:
        #     if order_details[order_detail].get_buyer() == username:
        #         new_order_details.append(order_details[order_detail])
        #         print(order_details[order_detail])
        # orders_data = [order.serialize() for order in new_order_details]
        orders_data = [order.serialize() for order in order_details.values()]
        return {'success': True, 'message': 'Get all order successfully', 'order_details': orders_data}
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
            
            return{'success': True, 'message': 'New information saved successfully'}
        else:   return{'success': False, 'message': 'Account not found'}
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

def handle_new_store_info(data_dict):
    try:
        new_info = data_dict.get('new_store_info') 
        store_id = new_info.get("store_id") 
        if store_id:
            user_name = new_info.get("user_name")
            user_id = new_info.get("user_id")
            store_name = new_info.get("store_name")
            email = new_info.get("email")
            phone_number = new_info.get("phone_number")
            description = new_info.get("description")
            picture = new_info.get("picture")
            store = root.stores[store_id]
            if store:
                store.store_name = store_name
                store.email = email
                store.phone_number = phone_number
                store.description = description
                store.picture = picture
                transaction.commit()
                return{'success': True, 'message': 'Save store new information saved successfully'}
        else: 
            new_store_id = generate_id("stores")
            store = Store(user_id,new_store_id,user_name,store_name,email,phone_number,description,picture)
            store[new_store_id] = store
            transaction.commit()
    except Exception as e:
        return {'success': False, 'message': str(e)}

def get_store(data_dict):
    try:
        store_id = data_dict.get('store_id')
        store = root.stores[store_id]
        if store:
            store_data = store.serialize()
            return{'success': True, 'store_data': store_data, 'message' : "Store found"}
        else:
            return {'success': False, 'message': 'Store not found'}
    except Exception as e:
        return {'success': False, 'message': str(e)}
def make_order(data_dict):
    try:
        root = connection.root
        orders = root.orders
        # Find the maximum existing ID
        order_id = generate_id('orders')
        product = data_dict.get('product')

        if product.get('product_id') in root.products:
            product_obj =  root.products[product.get('product_id')]
        else: raise ValueError("Product not found in database")
        buyer = data_dict.get('buyer')
        seller = data_dict.get('seller')
        status = data_dict.get('status')
        # Increment the maximum existing ID to get the next ID
        new_post = Order(order_id, product_obj,buyer,seller,status)
        orders[order_id] = new_post
        transaction.commit()
        
        return {'success': True, 'message': 'New order saved successfully'}
    
    except Exception as e:
        # Log the exception for debugging
        print(f"An error occurred: {e}")

        # Return error message if an exception occurs
        return {'success': False, 'message': str(e)}
    
def add_wishlist(data_dict):
    try:
        product = data_dict.get('product')
        username = data_dict.get('user_name')
        
        if product.get('product_id') in root.products:
            product_obj =  root.products[product.get('product_id')]
        else: raise ValueError("Product not found in database")
        
        account = root.accounts[username]
        if account:
            account.wishlist.append(product_obj)
            transaction.commit()
            return {'success': True, 'message': 'New wishlist saved successfully'}
        else:
            return {'success': False, 'message': 'Account not found'}
    except Exception as e:
        return {'success': False, 'message': str(e)}
    
def get_posts_by_name(data_dict):
    try:
        print("Received data:", data_dict)
        name = data_dict.get('name')
        posts = root.posts
        # print("Posts:", posts)
        
        search_results = []
        print("Searching for posts with name related to:", name)
        
        if posts:
            for post in posts:
                post_details = posts[post]
                product_name = post_details.get_product().get_pr_name()
                score = process.extractOne(name, [product_name], scorer=fuzz.token_set_ratio)
                print(f"Post Name: {product_name}, Search Query: {name}, Score: {score}")
                if score[1] >= 55:
                    search_results.append(post_details)
        else:
            print("No posts found.")
        
        posts_data = [x.serialize() for x in search_results]
        return {'success': True, 'post_details': posts_data}
    except Exception as e:
        traceback.print_exc()
        print("Error:", e)
        return {'success': False, 'message': 'Failed search'}

def get_tags_by_name(data_dict):
    try:
        name = data_dict.get('name')
        tags = root.tags
        tag_scores = {}

        search_results = []
        if tags:
            for tag in tags:
                tag_text = tag.get_tag_text()
                score = process.extractOne(name, [tag_text], scorer=fuzz.token_set_ratio)
                if score[1] >= 45:
                    tag_scores[tag] = score[1]

            # Sort the tags based on scores in descending order
            sorted_tags = sorted(tag_scores.items(), key=lambda x: x[1], reverse=True)

            # Limit the search results to 5 tags with the best scores
            for tag, score in sorted_tags[:5]:
                search_results.append(tag)
        else:
            print("No tag found")
        tags = [x.serialize() for x in search_results]
        return {'success': True, 'tags': tags}
    except Exception as e:
        traceback.print_exc()
        print("Error:", e)
        return {'success': False, 'message': 'Failed search'}

def get_all_tags():
    try:
        tags = root.tags
        sorted_tags = sorted(tags.values(), key=lambda x: x.times_used, reverse=True)
        top_5_tags = sorted_tags[:5]
        result = [tag.serialize() for tag in top_5_tags]
        return {'success': True, 'tags': result}
    except Exception as e:
        traceback.print_exc()
        print("Error:", e)
        return {'success': False, 'message': 'Couldnt retrieve tags'}

def save_slip(data_dict):
    try:
        order_id = data_dict.get("order_id")
        file_path = data_dict.get("file_path")
        orders = root.orders
        if order_id in orders:
            order = orders[order_id]
            order.slip_picture = file_path
            transaction.commit()
            return {'success': True, 'message': "Save slip in database"}
        else:
            print("Store not exits")
    except Exception as e:
        return {'success': False, 'message': e}
    
def update_status(data_dict):
    try:
        order_id = data_dict.get("order_id")
        status = data_dict.get("status")
        orders = root.orders
        if order_id in orders:
            order = orders[order_id]
            order.status = status
            transaction.commit()
            return {'success': True, 'message': "Updated Order Status"}
        else:
            print("Store not exits")
    except Exception as e:
        return {'success': False, 'message': e}
           
def handle_request(conn):
    try:
        print("Handling request...")
        # Receive data from the client
        data_dict = receive_large_data(conn)
        if not data_dict:
            print("No data received from client.")
            return
        print("Received data from client:", data_dict)
        action = data_dict.get('action')
        print("Received action:", action)
        if action == 'login':
            response = handle_login(data_dict)
            send_large_data(conn, response)

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
            response = get_all_orders(data_dict)
            send_large_data(conn, response)

        elif action == 'get_all_items':
            print("Calling get_all_items()")
            response = get_all_items(data_dict)
            send_large_data(conn, response)

        elif action == 'save_new_address':
            response = handle_new_address(data_dict)
            send_large_data(conn, response)
            
        elif action == "make_order":
            response = make_order(data_dict)
            send_large_data(conn, response)
            
        elif action == "add_wishlist":
            response = add_wishlist(data_dict)
            send_large_data(conn, response)
            
        elif action == "get_user_data":
            response = get_user_data(data_dict)
            send_large_data(conn, response)

        elif action == "check_store":
            print("Calling check store")
            response = check_store(data_dict)
            send_large_data(conn, response)

        elif action == "handle_new_store_info":
            response = handle_new_store_info(data_dict)
            send_large_data(conn, response)

        elif action == "get_store":
            print("Getting store")
            response = get_store(data_dict)
            send_large_data(conn, response)

        elif action == "get_posts_by_name":
            print("searching for posts by name")
            response = get_posts_by_name(data_dict)
            send_large_data(conn, response)
            
        elif action == "get_tags_by_name":
            response = get_tags_by_name(data_dict)
            send_large_data(conn, response)
        
        elif action == "get_all_tags":
            response = get_all_tags()
            send_large_data(conn, response)
            
        elif action == "save_slip":
            response = save_slip(data_dict)
            send_large_data(conn, response)

        elif action == "update_status":
            response = update_status(data_dict)
            send_large_data(conn, response)
            
        else:
            print("Invalid action")
            response = {'success': False, 'message': 'Invalid action'}
            
        print("Sending response to client:", response['message'])
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
    start_server('localhost', 9999)  # Change host and port as needed
