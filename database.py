import pandas as pd
from categorizer import *

class PandaDb():
    def __init__(self, filepath, sheet = 0, filetype = "xlsx"):
        self.filepath = filepath
        self.sheet = sheet
        self.filetype = filetype

        if filetype == "xlsx":
            self.transactions = pd.read_excel(filepath, sheet).drop(columns="Unnamed: 0")
        elif filetype == "csv":
            self.transactions = pd.read_csv(filepath, sheet)

    def export(self, export_filepath):
        if self.filetype == "xlsx":
            self.transactions.to_excel(export_filepath)
        elif self.filetype == "csv":
            self.transactions.to_csv(export_filepath)

    def categorize_list(self):
        for i in range(len(self.transactions)):
            self.transactions.at[i,"Kategori"] = categorize(self.transactions["Meddelande"][i])
        self.export(self.filepath)

    