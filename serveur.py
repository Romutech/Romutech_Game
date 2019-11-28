﻿import socket
import os
from server_classes.carte import Carte
from server_classes.robot import Robot
from server_classes.labyrinthe import Labyrinthe

hote = ''
port = 12800
cartes = []

for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            cartes.append(Carte(nom_carte, contenu))
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))

number_of_cards = i + 1

determine_position = True
win = False
loop = True
chosen_card = {}

while True:
	try:
		choose = int(input("\nEntrez un numéro de labyrinthe pour commencer à jouer : "))
		if 0 == choose :
			raise IndexError
		chosen_card = cartes[choose-1]
		labyrinth = Labyrinthe(chosen_card.labyrinthe, 'X', 'O', '.', 'U', carte.nom, chosen_card.height, chosen_card.width)
# ====================================================================
		connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connection.bind((hote, port))
		connection.listen(5)
		connection_with_client, infos_connexion = connection.accept()
		message_received = b""

		while determine_position:
			determine_position = False
			starting_position_of_the_robot = labyrinth.determine_starting_position_from_map(labyrinth.grille)
			robot = Robot(starting_position_of_the_robot)
			if labyrinth.positioning_is_validated((robot.ordinate, robot.abscissa)) == True:
				break
		data = labyrinth.show(labyrinth.grille, chosen_card.height, chosen_card.width, robot.get_position())
		text = "[labyrinth]" + data
		

		message_received = connection_with_client.recv(1024)
		message_received = message_received.decode()
		connection_with_client.send(text.encode())

		while win == False:
			message_received = connection_with_client.recv(1024)
			message_received = message_received.decode()
			
			i = 0

			

			order = message_received

			if order.upper() == 'Q':
				loop = False
				break

			if robot.the_direction_is_valid(order) == False or robot.number_of_move_box_is_valid(order) == False:
				continue
			
			if len(order[1:]) == 0:
				number_of_boxes = 1
			else:
				number_of_boxes = int(order[1:])

			i = 0

			letter = str(order[0])

			old_location = robot.get_position()

			while i < number_of_boxes:
				position = robot.displacement(letter, labyrinth)

				i += 1

				result = labyrinth.positioning_is_validated(position)

				if result == False:
					robot.set_position(old_location)
					text = "[status]" + "Impossible d'aller là !"
					break

				if result == True:
					robot.set_position(position)
					labyrinth.clear_the_robot_in_maze(labyrinth.grille)
					data = labyrinth.show(labyrinth.grille, chosen_card.height, chosen_card.width, position)

				text = "[labyrinth]" + data

			if labyrinth.is_win(position):
				win = True
				connection_with_client.send("[win] Bravo ! \nVous avez gagné !".encode())
				# connection_with_client.close()
				# connection.close()
				break
			if win == False:
				connection_with_client.send(text.encode())

		print("Fermeture de la connexion")
		connection_with_client.close()
		connection.close()
# ======================================================================
		while True:
			starting_position_of_the_robot = labyrinth.determine_starting_position_from_map(labyrinth.grille)
			robot = Robot(starting_position_of_the_robot)
			if labyrinth.positioning_is_validated((robot.ordinate, robot.abscissa)) == True:
				break
		
	except ValueError as e:
		print("Veuillez saisir un nombre")
	except IndexError as e:
		print("Veuillez saisir une carte qui existante")
	else:
		break
while win == False and loop :
	i = 0

