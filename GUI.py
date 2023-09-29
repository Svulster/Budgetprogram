import customtkinter as ctk
from importer import *
from settings import *

settings = App_Settings()
settings.load("./database/settings.pickle")

settings.settings_appearance_mode("Dark")
settings.save(f"{settings.database_folder}settings.pickle")

ctk.set_appearance_mode(settings.appearance_mode)
ctk.set_default_color_theme(settings.color_theme)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #Configure window
        self.title("Budgetprogram")
        self.geometry(f"{1100}x{700}")

        # configure grid layout (3x2)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((0,2), weight=0)
        self.grid_rowconfigure((0,1,4,5), weight=1)

        # Setup left sidebar
        self.sidebar_frame = ctk.CTkFrame(self,width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan = 6, sticky = "nsew")
        self.sidebar_frame.rowconfigure(4, weight=1)
        self.logo_label = ctk.CTkLabel(self.sidebar_frame,text="Menu",font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button1 = ctk.CTkButton(self.sidebar_frame, text="Import", command=lambda:[import_all(), self.popup_files("import", len(files))])
        self.sidebar_button1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button2 = ctk.CTkButton(self.sidebar_frame, text="Export", command=lambda:[self.popup_success("Export")])
        self.sidebar_button2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button3 = ctk.CTkButton(self.sidebar_frame, text="Upload", command=self.upload_window)
        self.sidebar_button3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button4 = ctk.CTkButton(self.sidebar_frame, text="Settings", command=self.settings_window)
        self.sidebar_button4.grid(row=4, column=0, padx=20, pady=10, sticky="s")

        # Setup overview frame
        self.overview_frame = ctk.CTkFrame(self, height=400, corner_radius=5)
        self.overview_frame.grid(row=0, column=1, rowspan = 5, sticky = "nsew", padx=10, pady=10)
        self.overview_frame.rowconfigure(1, weight=1)
        self.overview_frame.columnconfigure(1, weight=1)
        self.overview_label = ctk.CTkLabel(self.overview_frame,text="Yearly overview", font=ctk.CTkFont(size=14, weight="bold"))
        self.overview_label.grid(row=0, padx=20, pady=10)
        self.overview_option = ctk.CTkOptionMenu(self.overview_frame, dynamic_resizing=False, values=["2023"]) # Add function to determine what years are registred.
        self.overview_option.grid(row=0, column=1, sticky="e")

        # Setup transactions frame
        self.transactions_frame = ctk.CTkFrame(self, height=400, corner_radius=5,)
        self.transactions_frame.grid(row=5, column=1, rowspan=1, sticky = "nsew", padx=10, pady=10)
        self.transactions_frame.rowconfigure((1,2), weight=1)
        self.transactions_label = ctk.CTkLabel(self.transactions_frame,text="Transactions", font=ctk.CTkFont(size=14, weight="bold"))
        self.transactions_label.grid(row=0, padx=5, pady=5, sticky="w")
        self.transactions_seg_button = ctk.CTkSegmentedButton(self.transactions_frame)
        self.transactions_seg_button.grid(row=1, column=0, padx=5, pady=5, sticky="new")
        self.transactions_seg_button.configure(values=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
        self.transactions_seg_button.set("Jan")
        self.transactions_scrollable = ctk.CTkScrollableFrame(self.transactions_frame)
        self.transactions_scrollable.grid(row=2,column=0,padx=10,pady=10, sticky="nsew")
        self.transactions_scrollable.grid_columnconfigure(0,weight=1)

    def upload_window(self):
        upload_win = ctk.CTkToplevel()
        upload_win.wm_title("Upload")

    def settings_window(self):
        settings_win = ctk.CTkToplevel()
        settings_win.wm_title("Settings")

    def popup_files(self, action, no_files):
        popup = ctk.CTkToplevel()
        popup.wm_title(action)
        popup.geometry(f"{250}x{75}")
        if no_files == 1:
            popup_lbl = ctk.CTkLabel(popup, text=f"1 file {action}ed successfully!")
            popup_lbl.pack()
        else:
            popup_lbl = ctk.CTkLabel(popup, text=f"{no_files} files {action}ed successfully!")
            popup_lbl.pack()
        popup_btn = ctk.CTkButton(popup, text="OK", command=popup.destroy)
        popup_btn.pack()

    def popup_success(self, action):
        popup = ctk.CTkToplevel()
        popup.wm_title(action)
        popup.geometry(f"{250}x{75}")
        popup_lbl = ctk.CTkLabel(popup, text=f"{action} successful!")
        popup_lbl.pack()
        popup_btn = ctk.CTkButton(popup, text="OK", command=popup.destroy)
        popup_btn.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()