import pandas as pd
from categorizer import *

class PandaDb():
    def __init__(self, filepath, sheet = 0, filetype = "xlsx"):
        self.filepath = filepath
        self.sheet = sheet
        self.filetype = filetype

        if filetype == "xlsx":
            self.transactions = pd.read_excel(filepath, sheet)
            if "Unnamed: 0" in self.transactions.columns:
                self.transactions.drop(columns="Unnamed: 0", axis=1, inplace=True)                
        elif filetype == "csv":
            self.transactions = pd.read_csv(filepath, sheet)

    def __add__(self, dataframe2):
        dataframes = [self.transactions, dataframe2.transactions]
        return PandaDb(pd.concat(dataframes))

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
                print(str(self.transactions.at[i,"Datum"]) + " " + self.transactions.at[i,"Meddelande"] + " " + str(self.transactions.at[i,"Belopp"]))
                reply = input("Ändra kategori: ")
                if reply:
                    self.transactions.at[i,"Kategori"] = reply
            else:
                pass
        self.save_list(self.filepath)

    def sort_list(self):
        self.transactions.sort_values(by=["Datum"], inplace=True)
        self.save_list(self.filepath)

    def export(self, destination_filepath):
        # Exports the current file to a new excel file.
        pass

    def upload(self):
        # Uploads the current file to google sheets.
        pass