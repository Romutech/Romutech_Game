from tkinter import *

class GraphiqueInterface(Frame):
	def __init__(self, window, robot):
		Frame.__init__(self, window)
		self.window = window
		self.robot = robot
		self.window.title("Jeu du labyrinthe")
		self.window.minsize(1100, 755)
		self.show_title()
		self.show_margins()
		self.show_sections()
		
	def show_title(self):
		message_title = Label(self.window, text="BIENVENUE DANS LE JEU DU LABYRINTHE")
		message_title.pack()

	def show_margins(self):
		frame_margin_right = Frame(self.window)
		frame_margin_right.pack(side="right", fill=Y)
		label_margin_right = Label(frame_margin_right)
		label_margin_right.pack()
		frame_margin_left = Frame(self.window)
		frame_margin_left.pack(side="left")
		label_margin_left = Label(frame_margin_left)
		label_margin_left.pack()

	def show_sections(self):
		self.frame_right = Frame(self.window)
		self.frame_right.pack(side="right")
		self.frame_left = Frame(self.window)
		self.frame_left.pack(side="left")
		self.frame_bottom = Frame(self.window)
		self.frame_bottom.pack(side="bottom")

	def show_displacement(self):
		self.number_of_boxes = StringVar()
		frame_displacement = Frame(self.frame_right, bg="#DDE0FE")
		frame_displacement.pack()
		label_padding_right = Label(frame_displacement, bg="#DDE0FE", text="          ")
		label_padding_right.pack(side="right")
		label_padding_right = Label(frame_displacement, bg="#DDE0FE", text="          ")
		label_padding_right.pack(side="left")
		title_displacement = Label(frame_displacement, bg="#DDE0FE", text="DEPLACEMENT")
		title_displacement.pack()
		label_displacement = Label(frame_displacement, bg="#DDE0FE", text="Saisissez dans le champ jaune, le nombre de \n cases à se déplacer ET cliquez sur la direction")
		label_displacement.pack()
		ligne_texte = Entry(frame_displacement, bg="yellow", textvariable=self.number_of_boxes, width=4)
		ligne_texte.pack()
		label_displacement = Label(frame_displacement, bg="#DDE0FE")
		label_displacement.pack()
		exit_button = Button(frame_displacement, activeforeground="green", text="Nord", command=self.moving_the_robot_north)
		exit_button.pack(side="top", fill=Y)
		label_displacement = Label(frame_displacement, bg="#DDE0FE")
		label_displacement.pack(side="bottom")
		exit_button = Button(frame_displacement, activeforeground="green", text="Sud", command=self.moving_the_robot_south)
		exit_button.pack(side="bottom", fill=Y)
		exit_button = Button(frame_displacement, activeforeground="green", text="Est", command=self.moving_the_robot_east)
		exit_button.pack(side="right", fill=X)
		exit_button = Button(frame_displacement, activeforeground="green", text="Ouest", command=self.moving_the_robot_west)
		exit_button.pack(side="left", fill=X)

	def show_action_wall_door(self):
		frame_wall_door = Frame(self.frame_right, bg="#C7FBCC")
		frame_wall_door.pack()
		label_padding_right = Label(frame_wall_door, bg="#C7FBCC", text="          ")
		label_padding_right.pack(side="right")
		label_padding_right = Label(frame_wall_door, bg="#C7FBCC", text="          ")
		label_padding_right.pack(side="left")
		title_wall_door = Label(frame_wall_door, bg="#C7FBCC", text="MURER UNE PORTE")
		title_wall_door.pack()
		label_wall_a_door = Label(frame_wall_door, bg="#C7FBCC", text="Saisissez une direction et tentez de tranformer\nune porte à proximité, en mur")
		label_wall_a_door.pack()
		exit_button = Button(frame_wall_door, activeforeground="green", text="Nord", command=self.quit)
		exit_button.pack(side="top", fill=Y)
		label_wall_a_door = Label(frame_wall_door, bg="#C7FBCC")
		label_wall_a_door.pack(side="bottom")
		exit_button = Button(frame_wall_door, activeforeground="green", text="Sud", command=self.quit)
		exit_button.pack(side="bottom", fill=Y)
		exit_button = Button(frame_wall_door, activeforeground="green", text="Est", command=self.quit)
		exit_button.pack(side="right", fill=X)
		exit_button = Button(frame_wall_door, activeforeground="green", text="Ouest", command=self.quit)
		exit_button.pack(side="left", fill=X)

	def show_action_transform_door_into_wall(self):
		frame_transform_door_into_wall = Frame(self.frame_right, bg="#FCB4BB")
		frame_transform_door_into_wall.pack()
		label_padding_right = Label(frame_transform_door_into_wall, bg="#FCB4BB", text="          ")
		label_padding_right.pack(side="right")
		label_padding_right = Label(frame_transform_door_into_wall, bg="#FCB4BB", text="          ")
		label_padding_right.pack(side="left")
		title_transform_door_into_wall = Label(frame_transform_door_into_wall, bg="#FCB4BB", text="FAIRE UNE PORTE DANS LE MUR")
		title_transform_door_into_wall.pack()
		label_transform_door_into_wall = Label(frame_transform_door_into_wall, bg="#FCB4BB", text="Saisissez une direction et tentez de tranformer\nun mur à proximité, en porte")
		label_transform_door_into_wall.pack()
		exit_button = Button(frame_transform_door_into_wall, activeforeground="green", text="Nord", command=self.quit)
		exit_button.pack(side="top", fill=Y)
		label_transform_door_into_wall = Label(frame_transform_door_into_wall, bg="#FCB4BB")
		label_transform_door_into_wall.pack(side="bottom")
		exit_button = Button(frame_transform_door_into_wall, activeforeground="green", text="Sud", command=self.quit)
		exit_button.pack(side="bottom", fill=Y)
		exit_button = Button(frame_transform_door_into_wall, activeforeground="green", text="Est", command=self.quit)
		exit_button.pack(side="right", fill=X)
		exit_button = Button(frame_transform_door_into_wall, activeforeground="green", text="Ouest", command=self.quit)
		exit_button.pack(side="left", fill=X)

	def show_status(self):
		frame_status = Frame(self.frame_right, bg="#F1F0F0")
		frame_status.pack()
		label_padding_right = Label(frame_status, bg="#F1F0F0", text="         ")
		label_padding_right.pack(side="right")
		label_padding_right = Label(frame_status, bg="#F1F0F0", text="           ")
		label_padding_right.pack(side="left")
		labyrinthe = Label(frame_status, bg="#F1F0F0", text="STATUT")
		labyrinthe.pack()
		label_status = Label(frame_status, bg="#F1F0F0", text="                             Messages :                            ")
		label_status.pack()
		message_status = Label(frame_status, bg="#A09F9F", text="ex Attendez votre tour pour jouer")
		message_status.pack()
		label_status = Label(frame_status, bg="#F1F0F0", text="")
		label_status.pack()	
		
	def show_menu(self):
		frame_menu = Frame(self.frame_right, bg="#61DEFD")
		frame_menu.pack()
		label_padding_right = Label(frame_menu, bg="#61DEFD", text="          ")
		label_padding_right.pack(side="right")
		label_padding_right = Label(frame_menu, bg="#61DEFD", text="           ")
		label_padding_right.pack(side="left")
		title_menu = Label(frame_menu, bg="#61DEFD", text="MENU")
		title_menu.pack()
		label_menu = Label(frame_menu, bg="#61DEFD", text="                      Faites votre choix !                      ")
		label_menu.pack()
		exit_button = Button(frame_menu, text="Quitter la partie", overrelief="sunken", activeforeground="orange", command="")
		
		exit_button.pack(side="left")
		exit_button.flash()
		label_menu = Label(frame_menu, bg="#61DEFD", text=" ")
		label_menu.pack(side="left")
		exit_button = Button(frame_menu, text="Quitter le jeu", activeforeground="red", command="")
		exit_button.pack(side="right")
		label_menu = Label(frame_menu, bg="#61DEFD", text="")
		label_menu.pack()
		label_menu = Label(frame_menu, bg="#61DEFD", text="")
		label_menu.pack()

	def show_labyrinthe(self):
		frame_game = Frame(self.frame_left,)
		frame_game.pack()
		label_menu = Label(frame_game, text="LABYRINTHE")
		label_menu.pack(side="top")
		labyrinthe = Label(frame_game, bg="#000000", text="000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n000000 0000    X 0000 000. 0    X0 0000    X0 0000    X 00000 . 00 00.            000.          0.  0\n")
		labyrinthe.pack()

	def moving_the_robot_north(self):
		self.robot.moving_north(self.number_of_boxes)

	def moving_the_robot_south(self):
		self.robot.moving_south(self.number_of_boxes)

	def moving_the_robot_east(self):
		self.robot.moving_east(self.number_of_boxes)

	def moving_the_robot_west(self):
		self.robot.moving_west(self.number_of_boxes)
