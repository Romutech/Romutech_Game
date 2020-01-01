# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

from carte import Carte
from labyrinthe import Labyrinthe
from class_robot.robot import Robot

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
response = 'OUI'
chosen_card = {}

while True:
	try:
		choose = int(input("\nEntrez un numéro de labyrinthe pour commencer à jouer : "))

		if 0 == choose :
			raise IndexError
			
		chosen_card = cartes[choose-1]
		labyrinth = Labyrinthe(chosen_card.labyrinthe, 'X', 'O', '.', 'U', carte.nom, chosen_card.height, chosen_card.width)
		
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

labyrinth.show(labyrinth.grille, chosen_card.height, chosen_card.width, robot.get_position())

while win == False and loop :
	i = 0
	order = str(input("Saisissez une lettre pour déplacer le robot 'n' 's' 'e' 'o' ou saisissez 'q' pour quitter le jeu: "))

	if order.upper() == 'Q':
		print('Vous avez choisi de quitter le jeu, vous pourrez reprendre votre partie plus tard, si vous le souhaitez. \nAu revoir !')
		loop = False
		break

	if robot.the_direction_is_valid(order) == False or robot.number_of_move_box_is_valid(order) == False:
		continue

	if len(order[1:]) == 0:
		number_of_boxes = 1
	else:
		number_of_boxes = int(order[1:])

	while i < number_of_boxes:
		position = robot.displacement(order)

		if labyrinth.positioning_is_validated(position) == False:
			print("vous ne pouvez pas aller à cet endroit car un obstacle vous en empeche ! ")
			break

		robot.set_position(position)
		labyrinth.clear_the_robot_in_maze(labyrinth.grille)
		labyrinth.show(labyrinth.grille, chosen_card.height, chosen_card.width, robot.get_position())
		if labyrinth.is_win(position):
			backup_file.reset()
			win = True
			print('  *  *  *')
			print('   \ | /')
			print(" *-OOOO-*  *************************************")
			print("  OOO      * Félicitations ! Vous avez gagné ! *")
			print(" OO        *************************************")
			print("O\n")
			break

		i += 1
	