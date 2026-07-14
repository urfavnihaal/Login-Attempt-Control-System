import sqlite3
import hashlib
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("127.0.0.1", 50000))
server.listen()

print("Server is running on port 50000...")


def handle_connection(c):
    try:
        c.send("Username: ".encode())
        username = c.recv(1024).decode()

        c.send("Password: ".encode())
        password = c.recv(1024)
        password = hashlib.sha256(password).hexdigest()

        conn = sqlite3.connect("userdata.db")
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM userdata WHERE username=? AND password=?",
            (username, password)
        )

        if cur.fetchone():
            c.send("Login successful!".encode())
        else:
            c.send("Login failed!".encode())

        conn.close()

    except Exception as e:
        print("SERVER ERROR:", e)

    finally:
        c.close()


while True:
    client, addr = server.accept()
    print("Client connected:", addr)
    threading.Thread(target=handle_connection, args=(client,)).start()