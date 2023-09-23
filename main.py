from categorizer import *
from database import *
from GUI import App
from importer import * 

import_all()
export_all()

export_database = PandaDb(f"{export_folder}export.xlsx")
export_database.sort_list()

export_database.categorize_list()
update_categories_database(export_database)
export_database.change_category_all()

#if __name__ == "__main__":
#    app = App()
#    app.mainloop()