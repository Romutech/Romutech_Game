class Robot:
	def __ini__(seld, position):
		self.x = position[0]
		self.y = position[1]

	def moving_north(self, number_of_boxes):
		print("Déplacement vers le NORD de ", number_of_boxes.get(), " cases")
		
	def moving_south(self, number_of_boxes):
		print("Déplacement vers le SUD de ", number_of_boxes.get(), " cases")

	def moving_east(self, number_of_boxes):
		print("Déplacement vers l'EST de ", number_of_boxes.get(), " cases")
	
	def moving_west(self, number_of_boxes):
		print("Déplacement vers l'OUEST de ", number_of_boxes.get(), " cases")
