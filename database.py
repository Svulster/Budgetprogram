import pandas as pd
from categorizer import *

class PandaDb():
    def __init__(self, filepath, sheet = 0, filetype = "xlsx", account = "ICA"):
        self.filepath = filepath
        self.sheet = sheet
        self.filetype = filetype
        self.account = account

        if filetype == "xlsx":
            self.transactions = pd.read_excel(filepath, sheet).drop(columns="Unnamed: 0")
        elif filetype == "csv":
            self.transactions = pd.read_csv(filepath, sheet)

    def save_list(self, export_filepath):
        # Saves the current file.
        if self.filetype == "xlsx":
            self.transactions.to_excel(export_filepath)
        elif self.filetype == "csv":
            self.transactions.to_csv(export_filepath)

    def categorize_list(self):
        # Automatically changes the category value of all transactions in the list.
        for i in range(len(self.transactions)):
            self.transactions.at[i,"Kategori"] = categorize(self.transactions["Meddelande"][i])
        self.save_list(self.filepath)

    def change_category_all(self):
        # Loops through the list and changes the category value for a each transaction in the list. This will not update the categories database and will not effect the automatic categorization.
        for i in range(len(self.transactions)):
            if self.transactions.at[i,"Kategori"] == "Okategoriserad":
                print(self.transactions.at[i,"Datum"] + " " + self.transactions.at[i,"Meddelande"] + " " + self.transactions.at[i,"Belopp"])
                reply = input("Ändra kategori: ")
                if reply:
                    self.transactions.at[i,"Kategori"] = reply
            else:
                pass
        self.save_list(self.filepath)

    def export(self, destination_filepath):
        # Exports the current file to a new excel file.
        pass

    def upload(self):
        # Uploads the current file to google sheets.
        pass