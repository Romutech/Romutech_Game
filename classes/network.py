import socket

class Network:
	def __init__(self, hote, port):
		self.hote = hote
		self.port = port

	def connection(self):
		self.server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_connection.connect((self.hote, self.port))
		print("Connexion établie avec le serveur sur le port {}".format(self.port))

	def message_exchange_with_server(self, message):
		self.server_connection.send(message.encode())
		received_message = self.server_connection.recv(1024)
		return received_message.decode()
