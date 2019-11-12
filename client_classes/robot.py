from tkinter import *
from PIL import *

class Robot:
	def __init__(self, network):
		print("ok")
		self.network = network
		# self.x = position[0]
		# self.y = position[1]

	def displacement(self, direction, number_of_boxes):
		return self.network.message_exchange_with_server(direction.format(number_of_boxes))
