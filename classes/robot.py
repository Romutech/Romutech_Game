class Robot:
	def __init__(self, network):
		print("ok")
		self.network = network
		# self.x = position[0]
		# self.y = position[1]

	def moving_north(self, number_of_boxes):
		data = "Déplacement vers le NORD de {} cases".format(number_of_boxes.get())
		return self.network.message_exchange_with_server(data)
		
	def moving_south(self, number_of_boxes):
		data = "Déplacement vers le SUD de {} cases".format(number_of_boxes.get())
		return self.network.message_exchange_with_server(data)

	def moving_east(self, number_of_boxes):
		data = "Déplacement vers l'EST de {} cases".format(number_of_boxes.get())
		return self.network.message_exchange_with_server(data)
	
	def moving_west(self, number_of_boxes):
		# print("Déplacement vers l'OUEST de ", number_of_boxes.get(), " cases")
		data = "Déplacement vers l'OUEST de {} cases".format(number_of_boxes.get())
		return self.network.message_exchange_with_server(data)
