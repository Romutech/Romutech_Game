import socket

class Network:
	def __init__(self, hote, port):
		self.hote = hote
		self.port = port

	def connection(self):
		self.server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_connection.connect((self.hote, self.port))

	def sending(self, message):
		self.server_connection.send(message.encode())
		

	def receive(self):
		while True:
			msg_recu = self.server_connection.recv(1024)
			print(" le message est :")
			return msg_recu.decode() # Là encore, peut planter s'il y a des accents

