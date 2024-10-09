import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self, title, dimensions):
        super().__init__()
        self.title(title)
        self.full_screen()

        #window structure
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    def full_screen(self):
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")


