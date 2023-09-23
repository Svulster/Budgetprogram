import pandas as pd

filepath = "database/categories.xlsx"
sheet = 0

categories = pd.read_excel(filepath, sheet).drop(columns="Unnamed: 0")

def categorize(transaction_name):
    # Retrieves tha category value corresponding to given transaction name.
    if categories["Hyra"].eq(transaction_name).any():
        return "Hyra"
    elif categories["Lön"].eq(transaction_name).any():
        return "Lön"
    elif categories["Bidrag"].eq(transaction_name).any():
        return "Bidrag"
    elif categories["Sparande"].eq(transaction_name).any():
        return "Sparande"
    elif categories["Försäkring"].eq(transaction_name).any():
        return "Försäkring"
    elif categories["Överföringar"].eq(transaction_name).any():
        return "Intern överföring"
    elif categories["Mat"].eq(transaction_name).any():
        return "Mat"
    elif categories["Mat ute"].eq(transaction_name).any():
        return "Mat ute"
    elif categories["Hem"].eq(transaction_name).any():
        return "Hem"
    elif categories["Transport"].eq(transaction_name).any():
        return "Transport"
    elif categories["Abonnemang"].eq(transaction_name).any():
        return "Abonnemang"
    elif categories["Kläder"].eq(transaction_name).any():
        return "Kläder"
    elif categories["Barn"].eq(transaction_name).any():
        return "Barn"
    elif categories["Hälsa"].eq(transaction_name).any():
        return "Hälsa"
    elif categories["Nöje"].eq(transaction_name).any():
        return "Nöje"
    elif categories["Övriga inkomster"].eq(transaction_name).any():
        return "Övriga inkomster"
    elif categories["Hobby"].eq(transaction_name).any():
        return "Hobby"
    else:
        return "Okategoriserad"
    
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