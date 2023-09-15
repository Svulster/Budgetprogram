from categorizer import *
from database import *


imported_list = PandaDb("database/Kontoutdrag_exempel.xlsx")
imported_list.categorize_list()