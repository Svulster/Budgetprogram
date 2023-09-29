import pickle
from os.path import exists

class App_Settings:

    # Set initial settings here.
    def __init__(self):
        self.import_folder = "./import/"
        self.export_folder = "./export/"
        self.database_folder = "./database/"
        self.appearance_mode = "Dark"
        self.color_theme = "blue"

    # Property Getter and Setters to allow the application to
    # access the settings and change them
    @property
    def start_message(self):
        return self._start_message

    @start_message.setter
    def start_message(self, value):
        self._start_message = value

    def settings_appearance_mode(self, mode):
        self.appearance_mode = mode

    #Methods to save the settings to a file and load them from a file
    def save(self, filename):
        with open(filename, 'wb') as fo:
            pickle.dump(self, fo)

    def load(self, filename):
        if exists(filename):
            with open(filename, 'rb') as fi:
                newObj = pickle.load(fi)
            self.__dict__.update(newObj.__dict__)
