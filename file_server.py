import socket
import os

HOST = '127.0.0.1'   
PORT = 5001        

def send_file(conn, filename):
    if os.path.exists(filename):
        conn.send(b"FOUND")
        filesize = os.path.getsize(filename)
        conn.send(str(filesize).encode()) 
        with open(filename, 'rb') as f:
            chunk = f.read(1024)
            while chunk:
                conn.send(chunk)
                chunk = f.read(1024)
        print(f"[SENT] {filename} ({filesize} bytes)")
    else:
        conn.send(b"NOTFOUND")
        print(f"[ERROR] File not found: {filename}")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[SERVER STARTED] Listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr}")
        filename = conn.recv(1024).decode()
        print(f"[REQUEST] {filename} from {addr}")
        send_file(conn, filename)
        conn.close()

if __name__ == "__main__":
    start_server()
