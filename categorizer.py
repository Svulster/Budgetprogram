import pandas as pd

filepath = "database/categories.xlsx"
sheet = 0

categories = pd.read_excel(filepath, sheet).drop(columns="Unnamed: 0")

def categorize(transaction_name):
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
        return "Intern_överföring"
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
    else:
        return "Okategoriserad"
    
def update_category(transaction_name):
    print(transaction_name)
    cat = input("Ange kategori: ")
    if cat:
        for i in range(len(categories[cat])):
            if pd.isna(categories.at[i,cat]):
                categories.at[i, cat] = transaction_name
                break
    else:
        pass
    categories.to_excel(filepath)