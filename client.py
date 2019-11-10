from packages.graphique_interface import *
from classes.robot import *
from classes.network import *

network = Network("localhost", 12800)
network.connection()

robot = Robot(network)
graphique_interface = GraphiqueInterface(Tk(), robot)
graphique_interface.show_displacement()
graphique_interface.show_action_wall_door()
graphique_interface.show_action_transform_door_into_wall()
graphique_interface.show_status()
graphique_interface.show_menu()
graphique_interface.show_labyrinthe()
graphique_interface.mainloop()




# hote = "localhost"
# port = 12800

# msg_a_envoyer = b""
# while msg_a_envoyer != b"fin":
#     msg_a_envoyer = input("> ")
#     # Peut planter si vous tapez des caractères spéciaux
#     msg_a_envoyer = msg_a_envoyer.encode()
#     # On envoie le message
#     connexion_avec_serveur.send(msg_a_envoyer)
#     msg_recu = connexion_avec_serveur.recv(1024)
#     print(msg_recu.decode()) # Là encore, peut planter s'il y a des accents

# print("Fermeture de la connexion")
# connexion_avec_serveur.close()