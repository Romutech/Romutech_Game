# -*-coding:Utf-8 -*

"""This module contains the class Robot."""

class Robot:

    """Class representing a robot."""

    def __init__(self, starting_position_of_the_robot, representation, identifiant):

        """initializes the representation of a robot.
        Receives in parameter a tuple representing the starting position."""

        self.ordinate = starting_position_of_the_robot[0]
        self.abscissa = starting_position_of_the_robot[1]
        self.cardinal_points = {"North": 'N', "South": 'S', "East": 'E',"West": 'O'}
        self.representation = representation
        self.identifiant = identifiant


    def __repr__(self):
        return "identifiant : " + str(self.identifiant) + " abcissse : " + str(self.abscissa) + " ordonné : " + str(self.ordinate) + " representé par : " + str(self.representation)
    

    def __getitem__(self, position):
    	return (self.ordinate, self.abscissa)


    def displacement(self, direction):

        """Function allowing the robot to move according to the requested direction.
        It takes as parameter a string of characters"""

        i = 0
        ordinate = self.ordinate
        abscissa = self.abscissa

        letter = str(direction[0])
   
        if letter.upper() == self.cardinal_points['North']:
            ordinate -= 1
        elif letter.upper() == self.cardinal_points['South']:
            ordinate += 1
        elif letter.upper() == self.cardinal_points['East']:
            abscissa += 1
        elif letter.upper() == self.cardinal_points['West']:
            abscissa -= 1
        return (ordinate, abscissa)


    def set_position(self, position):

        """This function is used to define the position of the robot. This function is applied when the 
        position of the robot has been validated and no obstacle prevents the robot from being there."""

        self.ordinate = position[0]
        self.abscissa = position[1]


    def get_position(self):

        """This function returns the position of the robot in the form of a tuple.
        It takes as parameter a tuple (ordinate, abscissa)"""

        return (self.ordinate, self.abscissa)


    def the_direction_is_valid(self, direction):

        """This function is used to determine if the requested direction is valid and corresponds to a cardinal point.
        It takes as parameter a string of characters
        It returns a boolean"""

        message = "Vous n'avez pas saisie une direction valide, \nveuillez choisir \"n\" pour nord, \"s\" pour sud \"e\" pour est \"o\" pour ouest."
        try:
            letter = str(direction[0])
        except Exception as e:
            print(message)
            return False

        for key, value in self.cardinal_points.items():
            if value == letter.upper():
                return True
        print(message)
        return False


    def number_of_move_box_is_valid(self, direction):

        """This function makes it possible to determine that the user has not specified a number of boxes or has entered a number.
        It takes as parameter a string of characters
        It returns a boolean"""

        try:
            if len(direction[1:]) == 0:
                return True
            int(direction[1:])
        except Exception as e:
            print("Veuillez choisir une valeur numérique après la lettre indiquant la direction")
            return False
        return True
