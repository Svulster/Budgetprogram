from categorizer import *
from database import *
from GUI import App
from importer import * 

import_all()

#combine imported databases into one, place in the export folder
dataframes = []
for file in range(len(imported_databases)):
    dataframes.append(imported_databases[file].transactions)
dataframe = pd.concat(dataframes)
dataframe.to_excel(f"{export_folder}export.xlsx")

export_database = PandaDb(f"{export_folder}export.xlsx")
export_database.sort_list()


#imported_databases[0].categorize_list()
#update_categories_database(imported_databases[0])
#imported_databases[0].change_category_all()

#export_all(imported_databases)

#if __name__ == "__main__":
#    app = App()
#    app.mainloop()