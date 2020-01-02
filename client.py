import socket

import random
import sys
from threading import Thread
import time

hote = "localhost"
port = 12800

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))


class main(Thread):
    def __init__(self, connexion_avec_serveur):
        Thread.__init__(self)
        self.connexion_avec_serveur = connexion_avec_serveur
       
    def run(self):
        """Code à exécuter pendant l'exécution du thread."""

        
        msg_a_envoyer = b""
        while msg_a_envoyer != b"fin":
            msg_a_envoyer = input("> ")
            # Peut planter si vous tapez des caractères spéciaux
            msg_a_envoyer = msg_a_envoyer.encode()
            # On envoie le message
            self.connexion_avec_serveur.send(msg_a_envoyer)
        
                    
class listener(Thread):
    def __init__(self, connexion_avec_serveur):
        Thread.__init__(self)
        self.connexion_avec_serveur = connexion_avec_serveur

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        loop = True
        while loop:
            print("client ecoute ")
            msg_recu = self.connexion_avec_serveur.recv(1024)
            print(msg_recu.decode()) # Là encore, peut planter s'il y a des accents

            if msg_recu.decode() == "fin":
                print("Fermeture de la connexion")
                connexion_avec_serveur.close()



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
