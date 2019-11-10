import socket

class Network:
	def __init__(self, hote, port):
		self.hote = hote
		self.port = port

	def connection(self):
		self.server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_connection.connect((self.hote, self.port))
		print("Connexion établie avec le serveur sur le port {}".format(self.port))

	def send_message(self, message):
		print('zsd')
		self.server_connection.send(message.encode())

