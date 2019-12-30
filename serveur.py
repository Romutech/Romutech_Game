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

choose = int(input("\nEntrez un numéro de labyrinthe pour commencer à jouer : "))

chosen_card = cartes[choose-1]
labyrinth = Labyrinthe(chosen_card.labyrinthe, 'X', 'O', '.', 'U', carte.nom, chosen_card.height, chosen_card.width)


connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))
print("1")
serveur_lance = True
clients_connectes = []
message = "_"

while True:
	
	while loop == True:
		connexions_demandees, wlist, xlist = select.select([connexion_principale], [], [], 0.05)
		choice = input("on continue ? ")
		if choice == "non":
			loop = False


	for connexion in connexions_demandees:
		connexion_avec_client, infos_connexion = connexion.accept()
		clients_connectes.append(connexion_avec_client)

	message_received = b""

	
	print("2")
	

	while determine_position:
		starting_position_of_the_robot = labyrinth.determine_starting_position_from_map(labyrinth.grille)
		robot = Robot(starting_position_of_the_robot)
		if labyrinth.positioning_is_validated((robot.ordinate, robot.abscissa)) == True:
			break
	data = labyrinth.show(labyrinth.grille, chosen_card.height, chosen_card.width, robot.get_position())
	text = "[labyrinth]" + data

	print("3")
#while win == False:
	 
# ======================================================================
	while True:
		print("4")
		starting_position_of_the_robot = labyrinth.determine_starting_position_from_map(labyrinth.grille)
		robot = Robot(starting_position_of_the_robot)
		if labyrinth.positioning_is_validated((robot.ordinate, robot.abscissa)) == False:
			break

		print("5")
		clients_a_lire = []
		try:
			clients_a_lire, wlist, xlist = select.select(clients_connectes, [], [], 0.05)

		except select.error:
			pass
		else:
			print("6")
			for client in clients_a_lire:
				print("7")
				message_received = client.recv(1024)
				message_received = message_received.decode()

				message = "vous avez envoyé " + message_received
				print(message)


			for client in clients_connectes:
				print("8")
				client.send(text.encode())

	while win == False and loop :
		i = 0

print("Fermeture des connexions")
for client in clients_connectes:
	client.close()

connexion_principale.close()
