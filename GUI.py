import customtkinter as ctk
import tkinter as tk
import tkinter.messagebox

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #Configure window
        self.title("Budgetprogram")
        self.geometry(f"{1100}x{500}")

if __name__ == "__main__":
    app = App()
    app.mainloop()