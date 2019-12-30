import socket

import random
import sys
from threading import Thread
import time


hote = "localhost"
port = 12800

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))


class Client(Thread):
    def __init__(self, connexion_avec_serveur):
        Thread.__init__(self)
        self.connexion_avec_serveur = connexion_avec_serveur

    def run(self):
        connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connexion_avec_serveur.connect((hote, port))
        print("interface")
        
        msg_a_envoyer = b""
        while msg_a_envoyer != b"fin":
            msg_a_envoyer = input("> ")
            # Peut planter si vous tapez des caractères spéciaux
            msg_a_envoyer = msg_a_envoyer.encode()
            # On envoie le message
            self.connexion_avec_serveur.send(msg_a_envoyer)





class Listener(Thread):

    """Thread chargé simplement d'afficher une lettre dans la console."""

    def __init__(self, connexion_avec_serveur):
        Thread.__init__(self)
        self.connexion_avec_serveur = connexion_avec_serveur

    def run(self):
        
        print("Connexion établie avec le serveur sur le port {}".format(port))
        
        while True:
            msg_recu = self.connexion_avec_serveur.recv(1024)
            print(" le message est :")
            print(msg_recu.decode()) # Là encore, peut planter s'il y a des accents
        

# Création des threads
thread_2 = Listener(connexion_avec_serveur)
thread_1 = Client(connexion_avec_serveur)


# Lancement des threads
thread_2.start()
thread_1.start()


# Attend que les threads se terminent
thread_2.join()
thread_1.join()



