import socket

import random
import sys
from threading import Thread
import time

hote = "localhost"
port = 12800
program_execution = True

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))
print('\nEntrez "c" pour commencer à jouer.\n')


class main(Thread):
    def __init__(self, connexion_avec_serveur):
        Thread.__init__(self)
        self.connexion_avec_serveur = connexion_avec_serveur
        self.program_execution = True
       
    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        msg_a_envoyer = b""
        while msg_a_envoyer != b"fin" and self.program_execution:

            msg_a_envoyer = str(input(""))
            # Peut planter si vous tapez des caractères spéciaux
            msg_a_envoyer = msg_a_envoyer.encode()
            # On envoie le message
            self.connexion_avec_serveur.send(msg_a_envoyer)
            time.sleep(0.5)

    def stop_program_execution(self):
        self.program_execution = False
        return "program stop"
        

class listener(Thread):
    def __init__(self, connexion_avec_serveur, thread):
        Thread.__init__(self)
        self.connexion_avec_serveur = connexion_avec_serveur
        self.program_execution = True
        self.thread = thread

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""

        while self.program_execution:
            msg_recu = self.connexion_avec_serveur.recv(1024)

            if len(msg_recu) == 0:
                self.program_execution = False
                status = self.thread.stop_program_execution()
                break
            print(msg_recu.decode()) # Là encore, peut planter s'il y a des accents
            if msg_recu.decode() == "fin":
                print("Fermeture de la connexion")
                connexion_avec_serveur.close()


# Création des threads
thread_1 = main(connexion_avec_serveur)
thread_2 = listener(connexion_avec_serveur, thread_1)

# Lancement des threads
thread_1.start()
thread_2.start()

# Attend que les threads se terminent
thread_1.join()
thread_2.join()

print("Fermeture de la connexion")
connexion_avec_serveur.close()
