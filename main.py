from categorizer import *
from database import *
from GUI import App
from importer import * 

check_import_folder()
import_all()

imported_databases[0].change_category_all()

#if __name__ == "__main__":
#    app = App()
#    app.mainloop()