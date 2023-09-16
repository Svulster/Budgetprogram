import os
from database import PandaDb


import_folder = "./import/"

files = []

def check_import_folder():
	for file in os.listdir(import_folder):
		if file.endswith(".xlsx") or file.endswith(".csv"):
			files.append(file)
	return files

def import_file():
    imported_database = PandaDb(import_folder + files[0])
    return imported_database