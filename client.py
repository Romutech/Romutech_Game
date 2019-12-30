import socket

import random
import sys
from threading import Thread
import time


hote = "localhost"
port = 12800

class Client(Thread):
    def __init__(self):
        Thread.__init__(self)

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
            connexion_avec_serveur.send(msg_a_envoyer)
            msg_recu = connexion_avec_serveur.recv(1024)
            print(msg_recu.decode()) # Là encore, peut planter s'il y a des accents
        
        print("Fermeture de la connexion")
        connexion_avec_serveur.close()


class Listener(Thread):

    """Thread chargé simplement d'afficher une lettre dans la console."""

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connexion_avec_serveur.connect((hote, port))
        print("Connexion établie avec le serveur sur le port {}".format(port))
        
        while True:
            time.sleep(5)
            msg_recu = connexion_avec_serveur.recv(1024)
            print(msg_recu.decode()) # Là encore, peut planter s'il y a des accents
        
        print("Fermeture de la connexion")
        connexion_avec_serveur.close()

# Création des threads
thread_2 = Listener()
time.sleep(5)
thread_1 = Client()


# Lancement des threads
thread_2.start()
thread_1.start()


# Attend que les threads se terminent
thread_2.join()
thread_1.join()



