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
        print("Connexion établie avec le serveur sur le port {}".format(port))
        
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
        """Code à exécuter pendant l'exécution du thread."""
        i = 0
        while i < 20:
            sys.stdout.flush()
            attente = 1.2
            attente += random.randint(1, 60) / 100
            time.sleep(attente)
            i += 1
            print(attente)

# Création des threads
thread_1 = Client()
thread_2 = Listener()

# Lancement des threads
thread_1.start()
thread_2.start()

# Attend que les threads se terminent
thread_1.join()
thread_2.join()


