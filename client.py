from packages.graphique_interface import *

from classes.robot import *
import socket

robot = Robot()
graphique_interface = GraphiqueInterface(Tk(), robot)
graphique_interface.show_displacement()
graphique_interface.show_action_wall_door()
graphique_interface.show_action_transform_door_into_wall()
graphique_interface.show_status()
graphique_interface.show_menu()
graphique_interface.show_labyrinthe()
graphique_interface.mainloop()
graphique_interface.destroy()
