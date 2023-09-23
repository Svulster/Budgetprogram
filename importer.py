import os
from database import PandaDb
import pandas as pd

import_folder = "./import/"
export_folder = "./export/"

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
	check_import_folder()
	for file in range(len(files)):
		imported_databases.append(PandaDb(import_folder + files[file]))

def merge_all():														#Add possibility to append to an already existing export file. Check for, and avoid adding, duplicates.
	#combine imported databases into one, place in the export folder			
	dataframes = []
	for file in range(len(imported_databases)):
		dataframes.append(imported_databases[file].transactions)
	dataframe = pd.concat(dataframes)
	dataframe.sort_values(by=["Datum"], inplace=True)
	dataframe.to_excel(f"{import_folder}merged.xlsx")