import os
from database import PandaDb
import pandas as pd

import_folder = "./import/"
export_folder = "./export/"
database_folder = "./database/"

files = []
imported_databases = []

def check_import_folder():
	for file in os.listdir(import_folder):
		if file.endswith(".xlsx") or file.endswith(".csv"):
			if not file.startswith("merged"):
				files.append(file)
	return files

def import_file(i):
	imported_database = PandaDb(import_folder + files[i])
	return imported_database

def update_database(dataframe): #Exports a dataframe to the database folder. Creates a new file, and overwrites one if it already exists. Add possibility to append to an already existing export file. Check for, and avoid adding, duplicates.			
	dataframe.to_excel(f"{database_folder}transactions.xlsx")
	transactions = PandaDb(f"{database_folder}transactions.xlsx")
	transactions.categorize_list()
	transactions.save_list(f"{database_folder}transactions.xlsx")
	

def import_all():
	check_import_folder()
	for file in range(len(files)):
		imported_databases.append(PandaDb(import_folder + files[file]))
	dataframes = []
	for file in range(len(imported_databases)):
		dataframes.append(imported_databases[file].transactions)
	dataframe = pd.concat(dataframes)
	dataframe.sort_values(by=["Datum"], inplace=True, ascending=False)
	update_database(dataframe)