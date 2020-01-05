# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""

class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):

        """Initializes the representation of a map.
        Receives as parameter the name of a map in the form of a string of characters
        and a string representing the labyrinth."""

        self.nom = nom
        if isinstance(chaine, str):
            self.labyrinthe = self.creer_labyrinthe_depuis_chaine(chaine)

    def __repr__(self):
        return "<Carte {}>".format(self.nom)


    def creer_labyrinthe_depuis_chaine(self, chaine):

        """This function makes a maze from a string of characters and takes a string of characters.`
        She is returning a dictionary"""

        grille = {}
        i = 0 # abscissa
        j = 0 # ordinate

        for letter in chaine:
            if letter == '\n':
                self.width = i
                i = 0
                j += 1
            else:
                grille[(j,i)] = letter
                i += 1
            self.height = j + 1

        return grille

    def convert_labyrinth_from_dictionary_to_string(self, dictionnary, grid_height, grid_width):

        """converts dictionary-type labyrinth into a character string"""

        i = 0 # abscissa
        j = 0 # ordinate

        string_map = ""

        while j < grid_width:

            while i < grid_height:
                string_map += dictionnary[j, i]
                i += 1

            string_map += "\n"

            i = 0
            j += 1

        self.labyrinthe = self.creer_labyrinthe_depuis_chaine(string_map)

