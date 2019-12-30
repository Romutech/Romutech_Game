from tkinter import *
from packages.graphique_interface import *
from client_classes.robot import *
from client_classes.network import *

import socket
import sys
from threading import Thread
import time


network = Network("localhost", 12800)
network.connection()

robot = Robot(network)

graphique_interface = GraphiqueInterface(Tk(), robot, network)

class Client(Thread):
	def __init__(self, graphique_interface):
		Thread.__init__(self)
		self.graphique_interface = graphique_interface

	def run(self):
		self.graphique_interface.show_displacement()
		self.graphique_interface.show_action_wall_door()
		self.graphique_interface.show_action_transform_door_into_wall()
		self.graphique_interface.show_status()
		self.graphique_interface.show_menu()
		self.graphique_interface.show_labyrinthe()
		


class Listener(Thread):
	def __init__(self, graphique_interface):
		Thread.__init__(self)
		self.graphique_interface = graphique_interface

	def run(self):
		print("ok")
		self.graphique_interface.show()



# Création des threads

thread_1 = Client(graphique_interface)
thread_2 = Listener(graphique_interface)

# Lancement des threads
thread_1.start()
thread_2.start()


graphique_interface.mainloop()

# Attend que les threads se terminent
thread_1.join()
thread_2.join()


graphique_interface.mainloop()


