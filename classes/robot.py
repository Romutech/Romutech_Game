class Robot:
	def __init__(self, network):
		print("ok")
		self.network = network
		# self.x = position[0]
		# self.y = position[1]

	def moving_north(self, number_of_boxes):
		text = "Déplacement vers le NORD de {} cases".format(number_of_boxes.get())
		print(text)
		self.network.send_message(text)
		
	def moving_south(self, number_of_boxes):
		text = "Déplacement vers le SUD de {} cases".format(number_of_boxes.get())
		self.network.send_message(text)

	def moving_east(self, number_of_boxes):
		text = "Déplacement vers l'EST de {} cases".format(number_of_boxes.get())
		self.network.send_message(text)
	
	def moving_west(self, number_of_boxes):
		# print("Déplacement vers l'OUEST de ", number_of_boxes.get(), " cases")
		text = "Déplacement vers l'OUEST de {} cases".format(number_of_boxes.get())
		self.network.send_message(text)
