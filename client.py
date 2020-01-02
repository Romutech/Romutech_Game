import socket


import random
import sys
from threading import Thread
import time


hote = "localhost"
port = 12800

# ------------------------------------------------ SERVEUR -------------------------------------------------------------

# connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connexion_principale.bind((hote, port))
# connexion_principale.listen(1)
# print("Le client écoute à présent le serveur sur le port {}".format(port))

# serveur_lance = True
# clients_connectes = []

# ------------------------------------------------ FIN SERVEUR ---------------------------------------------------------

# --------------------------------------------------- CLIENT -----------------------------------------------------------

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))

# ------------------------------------------------ MULTI-TREADING ------------------------------------------------------

class main(Thread):
    def __init__(self, connexion_avec_serveur):
        Thread.__init__(self)
        self.connexion_avec_serveur = connexion_avec_serveur
       
    def run(self):
        """Code à exécuter pendant l'exécution du thread."""

        # --------------------------------------------------- CLIENT ---------------------------------------------------
        
        msg_a_envoyer = b""
        while msg_a_envoyer != b"fin":
            msg_a_envoyer = input("> ")
            # Peut planter si vous tapez des caractères spéciaux
            msg_a_envoyer = msg_a_envoyer.encode()
            # On envoie le message
            self.connexion_avec_serveur.send(msg_a_envoyer)
        
        # ----------------------------------------------- FIN CLIENT ---------------------------------------------------
                    
class listener(Thread):
    def __init__(self, connexion_avec_serveur):
        Thread.__init__(self)
        self.connexion_avec_serveur = connexion_avec_serveur

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        loop = True
        # -------------------------------------------- ECOUTE CLIENT ---------------------------------------------------
        while loop:
            print("client ecoute ")
            msg_recu = self.connexion_avec_serveur.recv(1024)
            print(msg_recu.decode()) # Là encore, peut planter s'il y a des accents

            if msg_recu.decode() == "fin":
                print("Fermeture de la connexion")
                connexion_avec_serveur.close()

        # ------------------------------------------- FIN ECOUTE CLIENT ------------------------------------------------

        # ------------------------------------------------ SERVEUR -----------------------------------------------------
       
        # while serveur_lance:
        #     # On va vérifier que de nouveaux clients ne demandent pas à se connecter
        #     # Pour cela, on écoute la connexion_principale en lecture
        #     # On attend maximum 50ms
        #     connexions_demandees, wlist, xlist = select.select([connexion_principale],
        #         [], [], 0.05)
            
        #     for connexion in connexions_demandees:
        #         connexion_avec_client, infos_connexion = connexion.accept()
        #         # On ajoute le socket connecté à la liste des clients
        #         clients_connectes.append(connexion_avec_client)
            
        #     # Maintenant, on écoute la liste des clients connectés
        #     # Les clients renvoyés par select sont ceux devant être lus (recv)
        #     # On attend là encore 50ms maximum
        #     # On enferme l'appel à select.select dans un bloc try
        #     # En effet, si la liste de clients connectés est vide, une exception
        #     # Peut être levée
        #     clients_a_lire = []
        #     try:
        #         clients_a_lire, wlist, xlist = select.select(clients_connectes,
        #                 [], [], 0.05)
        #     except select.error:
        #         pass
        #     else:
        #         # On parcourt la liste des clients à lire
        #         for client in clients_a_lire:
        #             # Client est de type socket
        #             msg_recu = client.recv(1024)
        #             # Peut planter si le message contient des caractères spéciaux
        #             msg_recu = msg_recu.decode()
        #             print("Reçu {}".format(msg_recu))
        #             client.send(b"5 / 5")
        #             if msg_recu == "fin":
        #                 serveur_lance = False
        
        # print("Fermeture des connexions")
        # for client in clients_connectes:
        #     client.close()
        
        #connexion_principale.close()

        # ------------------------------------------------ FIN SERVEUR -------------------------------------------------


# Création des threads
thread_1 = main(connexion_avec_serveur)
thread_2 = listener(connexion_avec_serveur)

# Lancement des threads
thread_1.start()
thread_2.start()

# Attend que les threads se terminent
thread_1.join()
thread_2.join()

print("Fermeture de la connexion")
connexion_avec_serveur.close()
