import pandas as pd

filepath = "database/categories.xlsx"
sheet = 0

categories = pd.read_excel(filepath, sheet).drop(columns="Unnamed: 0")
category_list = []


def categorize(transaction_name):
    # Retrieves tha category value corresponding to given transaction name.
    number_of_columns=len(categories.columns)
    counter = 0
    for col in categories.columns:
        if counter == number_of_columns-1:
            return "Okategoriserad"
        elif categories[col].eq(transaction_name).any():
            return col
        else:
            counter += 1

    
def update_category(transaction_name, cat):
    # Updates the categories database with the name of a single transaction
    if cat in categories.columns:
        counter = 0
        for i in range(len(categories[cat])):  
            counter += 1                         # How to append a value to the column if no cells are empty?
            if pd.isna(categories.at[i,cat]):
                categories.at[i, cat] = transaction_name
                break
            elif counter == len(categories[cat]):
                categories.at[counter, cat] = transaction_name
                break
    else:
        pass
    categories.to_excel(filepath)

def update_categories_database(database):
    # Updates the categories database for all transactions in a dataframe
    print("Updating the category database.")
    for i in range(len(database.transactions)):
        if database.transactions.at[i,"Kategori"] == "Okategoriserad":
            print(f"{database.transactions.at[i,'Datum']} {database.transactions.at[i,'Meddelande']} {database.transactions.at[i,'Belopp']}")
            reply = input("Update category database? ")
            if reply:
                if reply == "exit":
                    break
                else:
                    update_category(database.transactions.at[i,"Meddelande"], reply)
                    database.categorize_list()
            else:
                pass