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
