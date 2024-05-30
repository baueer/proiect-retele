import socket
import threading
import os
import time

recipient_list = ['Gigel', 'Marcel', 'Cornel']
other_servers = [('127.0.0.1', 12346), ('127.0.0.1', 12347)]
message_directory = 'messages'

if not os.path.exists(message_directory):
    os.makedirs(message_directory)

def handle_client(client_socket):
    try:
        message = client_socket.recv(1024).decode('utf-8')
        print(f"Received message: {message}")

        # Format mesaj: "destinatar;emitent;subiect;text")
        recipient, sender, subject, text = message.split(';')

        if recipient in recipient_list:
            timestamp = int(time.time())
            filename = f"{message_directory}/{recipient}/{timestamp}.txt"

            recipient_dir = f"{message_directory}/{recipient}"
            if not os.path.exists(recipient_dir):
                os.makedirs(recipient_dir)

            with open(filename, 'w') as f:
                f.write(f"From: {sender}\nSubject: {subject}\n\n{text}")
                print(f"Message from {sender} with subject {subject} saved successfully\n")

            client_socket.send(b"Message saved\n")
        else:
            routed = False
            for server_addr in other_servers:
                try:
                    other_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    other_server_socket.connect(server_addr)
                    other_server_socket.send(message.encode('utf-8'))

                    response = other_server_socket.recv(1024).decode('utf-8')
                    other_server_socket.close()

                    if response == "Message saved\n":
                        routed = True
                        client_socket.send(b"Message routed and saved\n")
                        break
                except Exception as e:
                    print(f"Could not connect to server {server_addr}: {e}")

            if not routed:
                client_socket.send(b"Recipient could not be found\n")
                print(f"Recipient {recipient} could not be found\n")
            else:
                print(f"Message from {sender} with subject {subject} routed and saved successfully\n")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 12345))
    server.listen(5)
    print("Server up and running on port 12345")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted incoming connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
