import socket
import pickle  # for serialization
from database import db, root  # Assuming your database setup is in backend.database module

def handle_login(data):
    email = data.get('email')
    password = data.get('password')

    # Retrieve user from the database based on email
    admins = root.admins
    for admin_id, admin in admins.items():
        if admin.get_email() == email and admin.get_password() == password:
            return {'success': True, 'message': 'Login successful'}
    
    return {'success': False, 'message': 'Invalid credentials'}

def handle_request(conn):
    try:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            data_dict = pickle.loads(data)
            if data_dict.get('action') == 'login':
                response = handle_login(data_dict)
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
    start_server('localhost', 9999)  # Change host and port as needed
