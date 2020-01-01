# -*-coding:Utf-8 -*

import pickle
import os

class BackupFile:

	"""This class represents a backup file"""

	def __init__(self, name_backup_file):
		self.name_backup_file = 'backup/' + name_backup_file


	def get_saved_data(self):

		"""This function allows you to recover the saved data"""
		
		with open(self.name_backup_file, 'rb') as fichier:
			mon_depickler = pickle.Unpickler(fichier)
			data = mon_depickler.load()
		return data


	def set_data_to_save(self, robot_position, maze_name, height, width):

		"""This function is used to define the information to be saved"""

		data = {
			"robot_position": robot_position,
			"maze_name": maze_name,
			"height": height,  
			"width": width
		}
	
		with open(self.name_backup_file, 'wb') as fichier:
			mon_pickler = pickle.Pickler(fichier)
			mon_pickler.dump(data)


	def reset(self):

		"""Resets the backup"""

		os.remove(self.name_backup_file)


	def backup_exists(self):
		
		"""Check if a backup exists"""

		try:
			with open(self.name_backup_file): pass
		except IOError:
			return False
		return True

	def loading_map(self, name_map):
		chemin = os.path.join("cartes", name_map + 'txt')
		nom_carte = name_map[:-1].lower()
		with open(chemin, "r") as fichier:
			content = fichier.read()
		return content
