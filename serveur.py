import socket
import select
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
	
	choose = int(input("\nEntrez un numéro de labyrinthe pour commencer à jouer : "))

	chosen_card = cartes[choose-1]
	labyrinth = Labyrinthe(chosen_card.labyrinthe, 'X', 'O', '.', 'U', carte.nom, chosen_card.height, chosen_card.width)

	#---------------------------------------------------------------------------------------------------------------=================================================







	#---------------------------------------------------------------------------------------------------------------=================================================

	while determine_position:
		starting_position_of_the_robot = labyrinth.determine_starting_position_from_map(labyrinth.grille)
		robot = Robot(starting_position_of_the_robot)
		if labyrinth.positioning_is_validated((robot.ordinate, robot.abscissa)) == True:
			break
	data = labyrinth.show(labyrinth.grille, chosen_card.height, chosen_card.width, robot.get_position())
	text = "[labyrinth]" + data
	


	connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connexion_principale.bind((hote, port))
	connexion_principale.listen(5)
	print("Le serveur écoute à présent sur le port {}".format(port))
	serveur_lance = True
	clients_connectes = []
	message = "_"
	connexions_demandees, wlist, xlist = select.select([connexion_principale], [], [], 0.05)
	for connexion in connexions_demandees:
		connexion_avec_client, infos_connexion = connexion.accept()
		clients_connectes.append(connexion_avec_client)

	message_received = b""

	clients_a_lire = []
	try:
		clients_a_lire, wlist, xlist = select.select(clients_connectes, [], [], 0.05)
	except select.error:
		pass
	else:
		for client in clients_a_lire:
			message_received = client.recv(1024)
			message_received = message_received.decode()

			message = "vous avez envoyé " + msg_recu
			print("Reçu {}".format(msg_recu))

		for client in clients_connectes:
			client.send(text.encode())
			client.send(message.encode())

	while win == False:
		for client in clients_a_lire:
			message_received = client.recv(1024)
			message_received = message_received.decode()
			order = message_received
		

			if order.upper() == 'Q':
				loop = False
				break

			if robot.number_of_move_box_is_valid(order) == False:
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

		
	# ======================================================================
		while True:
			starting_position_of_the_robot = labyrinth.determine_starting_position_from_map(labyrinth.grille)
			robot = Robot(starting_position_of_the_robot)
			if labyrinth.positioning_is_validated((robot.ordinate, robot.abscissa)) == True:
				break

	while win == False and loop :
		i = 0

print("Fermeture des connexions")
for client in clients_connectes:
	client.close()

connexion_principale.close()
