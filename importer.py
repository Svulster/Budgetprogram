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

def export_all(database_list):
	to_export = []
	for db in database_list:
		to_export.append(db.transactions)
	export_dataframe = pd.concat([export_dataframe, to_export], ignore_index=True)
	export_dataframe.sort_values(by=["Datum"])
	export_dataframe.to_excel(export_folder)