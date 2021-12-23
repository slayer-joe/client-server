import socket

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def send(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, self.port))
        sock.send(bytes('modules/test_file.txt', encoding = 'UTF-8'))
        data = sock.recv(4096).decode()
        print(data)
        with open('new_file.txt', 'w') as f:
            f.write(data)
        sock.close()

client = Client('127.0.0.1', 3000)
client.send()

