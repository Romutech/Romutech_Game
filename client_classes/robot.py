from tkinter import *
from PIL import *

class Robot:
	def __init__(self, network):
		self.network = network
		# self.x = position[0]
		# self.y = position[1]

	def displacement(self, direction, number_of_boxes):
		return self.network.sending(direction+number_of_boxes.get())
