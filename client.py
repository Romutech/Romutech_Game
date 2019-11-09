# import socket
from tkinter import *

# hote = "localhost"
# port = 12800

# connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connexion_avec_serveur.connect((hote, port))
# print("Connexion établie avec le serveur sur le port {}".format(port))

# -------------------------
window = Tk()

window.title("Jeu du labyrinthe")
window.minsize(1000, 650)

message_title = Label(window, text="BIENVENU DANS LE JEU DU LABYRINTHE")
message_title.pack()

frame_right = Frame(window)
frame_right.pack(side="right")

###############
# DEPLACEMENT #
###############
frame_displacement = Frame(frame_right, bg="#DDE0FE")
frame_displacement.pack()
title_displacement = Label(frame_displacement, bg="#DDE0FE", text="DEPLACEMENT")
title_displacement.pack()
label_displacement = Label(frame_displacement, bg="#DDE0FE", text="Saisissez dans le champ jaune, le nombre de \n cases à se déplacer ET cliquez sur la direction")
label_displacement.pack()

var_texte = StringVar()
ligne_texte = Entry(frame_displacement, bg="yellow", textvariable=var_texte, width=4)
ligne_texte.pack()
label_displacement = Label(frame_displacement, bg="#DDE0FE")
label_displacement.pack()

bouton_quitter = Button(frame_displacement, fg="red", text="Nord", command=window.quit)
bouton_quitter.pack(side="top", fill=Y)
label_displacement = Label(frame_displacement, bg="#DDE0FE")
label_displacement.pack(side="bottom")
bouton_quitter = Button(frame_displacement, fg="red", text="Sud", command=window.quit)
bouton_quitter.pack(side="bottom", fill=Y)
bouton_quitter = Button(frame_displacement, fg="red", text="Est", command=window.quit)
bouton_quitter.pack(side="right", fill=X)
bouton_quitter = Button(frame_displacement, fg="red", text="Ouest", command=window.quit)
bouton_quitter.pack(side="left", fill=X)

###################
# MURER UNE PORTE #
###################
frame_wall_door = Frame(frame_right, bg="#C7FBCC")
frame_wall_door.pack()
title_wall_door = Label(frame_wall_door, bg="#C7FBCC", text="MURER UNE PORTE")
title_wall_door.pack()
label_wall_a_door = Label(frame_wall_door, bg="#C7FBCC", text="Saisissez une direction et tentez de tranformer\nune porte à proximité, en mur")
label_wall_a_door.pack()
bouton_quitter = Button(frame_wall_door, fg="red", text="Nord", command=window.quit)
bouton_quitter.pack(side="top", fill=Y)
label_wall_a_door = Label(frame_wall_door, bg="#C7FBCC")
label_wall_a_door.pack(side="bottom")
bouton_quitter = Button(frame_wall_door, fg="red", text="Sud", command=window.quit)
bouton_quitter.pack(side="bottom", fill=Y)
bouton_quitter = Button(frame_wall_door, fg="red", text="Est", command=window.quit)
bouton_quitter.pack(side="right", fill=X)
bouton_quitter = Button(frame_wall_door, fg="red", text="Ouest", command=window.quit)
bouton_quitter.pack(side="left", fill=X)


###############################
# FAIRE UNE PORTE DANS LE MUR #
###############################
frame_transform_door_into_wall = Frame(frame_right, bg="#FCB4BB")
frame_transform_door_into_wall.pack()
title_transform_door_into_wall = Label(frame_transform_door_into_wall, bg="#FCB4BB", text="FAIRE UNE PORTE DANS LE MUR")
title_transform_door_into_wall.pack()
label_transform_door_into_wall = Label(frame_transform_door_into_wall, bg="#FCB4BB", text="Saisissez une direction et tentez de tranformer\nune porte à proximité, en mur")
label_transform_door_into_wall.pack()
bouton_quitter = Button(frame_transform_door_into_wall, fg="red", text="Nord", command=window.quit)
bouton_quitter.pack(side="top", fill=Y)
label_transform_door_into_wall = Label(frame_transform_door_into_wall, bg="#FCB4BB")
label_transform_door_into_wall.pack(side="bottom")
bouton_quitter = Button(frame_transform_door_into_wall, fg="red", text="Sud", command=window.quit)
bouton_quitter.pack(side="bottom", fill=Y)
bouton_quitter = Button(frame_transform_door_into_wall, fg="red", text="Est", command=window.quit)
bouton_quitter.pack(side="right", fill=X)
bouton_quitter = Button(frame_transform_door_into_wall, fg="red", text="Ouest", command=window.quit)
bouton_quitter.pack(side="left", fill=X)

##########
# STATUT #
##########
frame_status = Frame(frame_right, bg="#F1F0F0")
frame_status.pack()
title_status = Label(frame_status, bg="#F1F0F0", text="STATUT")
title_status.pack()
label_status = Label(frame_status, bg="#F1F0F0", text="                             Messages :                            ")
label_status.pack()
message_status = Label(frame_status, bg="#A09F9F", text="ex Attendez votre tour pour jouer")
message_status.pack()
label_status = Label(frame_status, bg="#F1F0F0", text="")
label_status.pack()

window.mainloop()

# --------------------------


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