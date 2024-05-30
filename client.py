import socket

server_addr = ('127.0.0.1', 12345)

def send_message(recipient, sender, subject, text):
    message = f"{recipient};{sender};{subject};{text}"
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(server_addr)
    client.send(message.encode('utf-8'))

    response = client.recv(1024).decode('utf-8')
    print(f"\nServer response: {response}")

    client.close()


if __name__ == "__main__":
    try:
        while True:
            recipient = input("Recipient: ")
            sender = input("Sender: ")
            subject = input("Subject: ")
            text = input("Text: ")

            send_message(recipient, sender, subject, text)
    except KeyboardInterrupt:
        print("\nClient closed")
