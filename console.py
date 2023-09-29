from importer import *
from database import *
from settings import *
from categorizer import *

settings = App_Settings()
settings.load("./database/settings.pickle")

def menu():
    print("Main menu")
    choice = input("? ")
    if choice == "import":
        import_all()


menu()
