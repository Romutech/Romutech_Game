# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os
import socket
import select
import time

from carte import Carte
from labyrinthe import Labyrinthe
from class_robot.robot import Robot

hote = ''
port = 12800 

# On charge les cartes existantes
cartes = []
car = []
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            # Création d'une carte, à compléter
            cartes.append(Carte(nom_carte, contenu))
            car.append(Carte(nom_carte, contenu))

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))

number_of_cards = i + 1

#continuation of the program

win = False
loop = True
step = 1
chosen_card = {}
copy_chosen_card_grille = {}
while True:
	try:
		choose = int(input("\nEntrez un numéro de labyrinthe pour commencer à jouer : "))
		if 0 == choose :
			raise IndexError

		chosen_card = cartes[choose-1]
		copy_chosen_card_grille = car[choose-1]

	except ValueError as e:
		print("Veuillez saisir un nombre")
	except IndexError as e:
		print("Veuillez saisir une carte qui existante")
	else:
		break

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))


clients_connectes = []
robot = {}
robot_representations = ['X', 'x', 'Y', 'y', 'Z']
i = 0
msg_recu = ""
index = 0
move = True

while win == False and loop:
	if step == 1:
		connexions_demandees, wlist, xlist = select.select([connexion_principale], [], [], 0.05)

		for connexion in connexions_demandees:
			connexion_avec_client, infos_connexion = connexion.accept()
			clients_connectes.append(connexion_avec_client)
		
		try:
			clients_a_lire, wlist, xlist = select.select(clients_connectes, [], [], 0.05)
		except select.error:
			pass
		else:
			for client in clients_a_lire:
				msg_recu = client.recv(1024)
				msg_recu = msg_recu.decode()

				if msg_recu.upper() == 'C':
					step = 2
					client.send("\nLa partie commence !\n".encode())
					break

	if step == 2:
		labyrinth = Labyrinthe(chosen_card.labyrinthe, 'O', '.', 'U', carte.nom, chosen_card.height, chosen_card.width)
		num = 0

		while num < len(clients_connectes):
			starting_position_of_the_robot = labyrinth.determine_starting_position_from_map(labyrinth.grille)

			bot = Robot(starting_position_of_the_robot, robot_representations[num], clients_connectes[num].getpeername()[1])

			robot[clients_connectes[num].getpeername()[1]] = {}
			robot[clients_connectes[num].getpeername()[1]]['object'] = bot
			robot[clients_connectes[num].getpeername()[1]]['identifiant'] = bot.identifiant
			robot[clients_connectes[num].getpeername()[1]]['representation'] = bot.representation
			robot[clients_connectes[num].getpeername()[1]]['ordinate'] = bot.ordinate
			robot[clients_connectes[num].getpeername()[1]]['abscissa'] = bot.abscissa
			

			if labyrinth.positioning_is_validated((robot[clients_connectes[num].getpeername()[1]]['ordinate'], robot[clients_connectes[num].getpeername()[1]]['abscissa'])) == True:
				num += 1



		message = labyrinth.show(labyrinth.grille, chosen_card.height, chosen_card.width, robot, chosen_card.labyrinthe)


		for client in clients_connectes:
			client.send(message.encode())
		num = 0

		while num < len(clients_connectes):
			message = "Votre robot est celui là : " + str(robot[clients_connectes[num].getpeername()[1]]['representation'])
			clients_connectes[num].send(message.encode())
			num += 1

		for client in clients_connectes:
			if clients_connectes[index].getpeername()[1] != client.getpeername()[1]:
				client.send("\n\nAttendez votre tour pour jouer ! \n".encode())
		
		clients_a_lire = []

		try:
			clients_a_lire, wlist, xlist = select.select(clients_connectes, [], [], 0.05)
			
		except select.error:
			pass
		else:
			msg_recu = ""

			while True:
				client = clients_connectes[index]
				client.send("\nC'est à votre tour de jouer. \nSaisissez une lettre pour déplacer le robot 'n' 's' 'e' 'o',  \n'm' suivi de la direction pour murer une porte, 'p' suivi de la direction pour percer une porte \nou saisissez 'q' pour quitter le jeu: ".encode())
				msg_recu = client.recv(1024)
				order = msg_recu.decode()
				i = 0

				if order.upper() == 'Q':
					print("\n\nFin du jeu ! Au revoir !\n")
					loop = False
					break

				if order[0].upper() == 'M':
					message = robot[client.getpeername()[1]]['object'].wall(order[1], labyrinth)
					order = ''
					client.send(message.encode())

				if order[0].upper() == 'P':
					message = robot[client.getpeername()[1]]['object'].door(order[1], labyrinth)
					order = ''
					client.send(message.encode())
	
				if len(order) != 0:
					if robot[client.getpeername()[1]]['object'].the_direction_is_valid(order) == False or robot[client.getpeername()[1]]['object'].number_of_move_box_is_valid(order) == False:
						continue

					if len(order[1:]) == 0:
						number_of_boxes = 1
					else:
						number_of_boxes = int(order[1:])

					move = False

					while i < number_of_boxes:

						position = robot[client.getpeername()[1]]['object'].displacement(order)

						if labyrinth.is_win(position):
							win = True
							message = "\n\n  *  *  *\n   \ | /\n *-OOOO-* \n  OOO      La partie a été gagnée par " + str(robot[client.getpeername()[1]]['representation']) + "\n OO        \nO\n"
							
							for client in clients_connectes:
								client.send(message.encode())
								client.send("fin".encode())
							break

						if labyrinth.positioning_is_validated(position) == False:
							client.send("\n\nvous ne pouvez pas aller à cet endroit car un obstacle vous en empeche ! \n".encode())
							break

						robot[client.getpeername()[1]]['object'].set_position(position)
						robot[client.getpeername()[1]]['ordinate'] = robot[client.getpeername()[1]]['object'].ordinate
						robot[client.getpeername()[1]]['abscissa'] = robot[client.getpeername()[1]]['object'].abscissa


						labyrinth.clear_the_robot_in_maze(labyrinth.grille, robot[client.getpeername()[1]]['representation'], copy_chosen_card_grille.labyrinthe)
						move = True
						i += 1

				if win == False:
					message = labyrinth.show(labyrinth.grille, chosen_card.height, chosen_card.width, robot, chosen_card.labyrinthe)
				
				if win:
					break

				for c in clients_connectes:
					if len(msg_recu) > 0:
						c.send(message.encode())

				for client in clients_connectes:
					i = index + 1

					if i >= len(clients_connectes):
						i = 0
					if clients_connectes[i].getpeername()[1] != client.getpeername()[1]:
						client.send("\nAttendez votre tour pour jouer !\n".encode())

				if move == True:
					index += 1
					move = False
				
				if index >= len(clients_connectes):
					index = 0

print("Fermeture des connexions")

for client in clients_connectes:
	client.close()

connexion_principale.close()
