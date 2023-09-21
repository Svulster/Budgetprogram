from categorizer import *
from database import *
from GUI import App
from importer import * 

check_import_folder()
import_all()

imported_databases[0].categorize_list()
update_categories_database(imported_databases[0])

#if __name__ == "__main__":
#    app = App()
#    app.mainloop()