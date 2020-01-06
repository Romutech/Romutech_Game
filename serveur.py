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
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            # Création d'une carte, à compléter
            cartes.append(Carte(nom_carte, contenu))

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))

number_of_cards = i + 1

#continuation of the program

win = False
loop = True
first = True
response = 'OUI'
chosen_card = {}
first = True

while True:
	try:
		choose = int(input("\nEntrez un numéro de labyrinthe pour commencer à jouer : "))

		if 0 == choose :
			raise IndexError

		chosen_card = cartes[choose-1]
	except ValueError as e:
		print("Veuillez saisir un nombre")
	except IndexError as e:
		print("Veuillez saisir une carte qui existante")
	else:
		break

# ------------------------------------ PARTIE SERVEUR ------------------------------------------------------------------

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))


serveur_lance = True
clients_connectes = []
robot = {}
robot_representations = ['X', 'x', 'Y', 'y', 'Z']
i = 0
num = 0

# ------------------------------------ FIN PARTIE SERVEUR --------------------------------------------------------------

msg_recu = ""

while win == False and loop and serveur_lance:

# ------------------------------------ PARTIE SERVEUR ------------------------------------------------------------------

################################### FIRST ######################################
	if first:
		first = False
		input('Appuyez sur une touche pour lancer la partie')

		while i < 6:
			connexions_demandees, wlist, xlist = select.select([connexion_principale], [], [], 0.05)

			for connexion in connexions_demandees:
				connexion_avec_client, infos_connexion = connexion.accept()
				clients_connectes.append(connexion_avec_client)
			i += 1

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

################################ FIN FIRST #####################################

	clients_a_lire = []

	try:
		clients_a_lire, wlist, xlist = select.select(clients_connectes, [], [], 0.05)
	except select.error:
		pass
	else:
		msg_recu = ""

		for client in clients_a_lire:
			msg_recu = client.recv(1024)
			msg_recu = msg_recu.decode()
			print("Reçu {}".format(msg_recu))

			order = msg_recu
			i = 0

			if order.upper() == 'Q':
				print('Fin du jeu ! Au revoir !')
				loop = False
				break

			if robot[client.getpeername()[1]]['object'].the_direction_is_valid(order) == False or robot[client.getpeername()[1]]['object'].number_of_move_box_is_valid(order) == False:
				continue

			if len(order[1:]) == 0:
				number_of_boxes = 1
			else:
				number_of_boxes = int(order[1:])

			while i < number_of_boxes:
				position = robot[client.getpeername()[1]]['object'].displacement(order)

				if labyrinth.positioning_is_validated(position) == False:
					client.send("vous ne pouvez pas aller à cet endroit car un obstacle vous en empeche ! ".encode())
					break

				robot[client.getpeername()[1]]['object'].set_position(position)
				robot[client.getpeername()[1]]['ordinate'] = robot[client.getpeername()[1]]['object'].ordinate
				robot[client.getpeername()[1]]['abscissa'] = robot[client.getpeername()[1]]['object'].abscissa
				labyrinth.clear_the_robot_in_maze(labyrinth.grille)
				message = labyrinth.show(labyrinth.grille, chosen_card.height, chosen_card.width, robot)

				if labyrinth.is_win(position):
					win = True
					message = "\n\n  *  *  *\n   \ | /\n *-OOOO-*  *************************************\n  OOO      * Félicitations ! Vous avez gagné ! *\n OO        *************************************\nO\n"

				for c in clients_connectes:
					if len(msg_recu) > 0:
						c.send(message.encode())

				i += 1


		if len(msg_recu) > 0:
			if msg_recu == "fin":
				serveur_lance = False
# ------------------------------------ FIN PARTIE SERVEUR --------------------------------------------------------------



# toto deplacer dans client => str(input("Saisissez une lettre pour déplacer le robot 'n' 's' 'e' 'o' ou saisissez 'q' pour quitter le jeu: "))

# ------------------------------------ PARTIE SERVEUR ------------------------------------------------------------------

print("Fermeture des connexions")

for client in clients_connectes:
	client.close()

connexion_principale.close()

# ------------------------------------ FIN PARTIE SERVEUR --------------------------------------------------------------


