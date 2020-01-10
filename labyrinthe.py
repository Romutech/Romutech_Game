# -*-coding:Utf-8 -*
from random import randrange

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, labyrinthe, obstacles, doors, exit, name_map, width, height):

        """Initializes the representation of a labyrinth.
        Receives in parameter:
        - a labyrinth in the form of a dictionary
        - the graphic representation of a robot
        - the graphic representation of the obstacles
        - the graphic representation of the doors
        - the graphic representation of the labyrinth's exit"""

        self.robot = 'X'
        self.grille = labyrinthe
        self.obstacles = obstacles
        self.doors = doors
        self.exit = exit
        self.name_map = name_map
        self.width = width
        self.height = height

    def show(self, grid_map, grid_height, grid_width, robots):

        """This function displays the labyrinth
        It takes in parameters a dictionary representing the labyrinth,
        the labyrinth width in the form of an int,
        the height in the form of an int,
        and the position of the robot in the form of a tuple"""

        robot_present = False

        i = 0 # abscissa
        j = 0 # ordinate
        lab = "\n"
        while j < grid_height -1:
            while i < grid_width:
                for robot in robots:
                    if j == robots[robot]['ordinate'] and i == robots[robot]['abscissa']:
                        self.grille[(j,i)] = robots[robot]['representation']
                        lab += robots[robot]['representation']
                        robot_present = True
                
                if robot_present == False:
                    self.grille[(j,i)] =  grid_map[j, i]
                    lab += grid_map[j, i]
                robot_present = False
                i += 1
            lab += "\n"
            i = 0
            j += 1
        lab += "\n"

        return lab


    def determine_starting_position_from_map(self, labyrinth):

        """Determines the robot's starting position through the card.
        It takes as parameter the labyrinth dictionary
        Returns the position of the robot in a tuple (ordinate, abcisse)"""

        for value in labyrinth:
            if labyrinth[value] == self.robot:
                return value[0], value[1]

        # if the robot was not found on the map, this position is determined randomly
        print ("définition aléatoire de la position du robot")
        return (randrange(0, self.width -1), randrange(0, self.height -1))


    def clear_the_robot_in_maze(self, labyrinth, robot):

        """Erase robot in labyrinth and It takes as parameter the labyrinth dictionary"""

        for value in labyrinth:
            if labyrinth[value] == robot:
                self.grille[value] = ' '


    def positioning_is_validated(self, position):

        """Check that the position is valid and take as parameter the dictionary labyrinth.
        It returns a boolean."""

        if self.grille[position] == ' ' or self.grille[position] == '.' or self.grille[position] == 'U':
            return True
        return False


    def is_win(self, position):

        """Determine if the player has won and takes a position in the form of a tuple.
        It returns a boolean."""

        if self.grille[position] == self.exit:
            return True
        return False
