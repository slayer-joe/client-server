import socket


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start(self):
        srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        srv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv_sock.bind((self.host, self.port))
        srv_sock.listen(3)
        
        while True:
            connect, addr = srv_sock.accept()
            data = connect.recv(4096).decode()
            with open(data, 'r') as file:
                text = file.read()
                connect.send(text.encode())
            connect.close()

server = Server('127.0.0.1', 3000)
server.start()