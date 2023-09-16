from categorizer import *
from database import *
from GUI import App
from importer import * 

check_import_folder()
imported_list = import_file()

#imported_list = PandaDb("database/Kontoutdrag_exempel.xlsx")
update_categories_database(imported_list)

#if __name__ == "__main__":
#    app = App()
#    app.mainloop()