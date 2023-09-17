import os
from database import PandaDb


import_folder = "./import/"

files = []
imported_databases = []

def check_import_folder():
	for file in os.listdir(import_folder):
		if file.endswith(".xlsx") or file.endswith(".csv"):
			files.append(file)
	return files

def import_file(i):
    imported_database = PandaDb(import_folder + files[i])
    return imported_database

def import_all():
	for file in range(len(files)):
		imported_databases.append(PandaDb(import_folder + files[file]))