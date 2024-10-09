import customtkinter as ctk
from . import main_frame

class App(ctk.CTk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.full_screen()

        #window structure
        self.rowconfigure(0, weight=1, uniform='a')
        self.columnconfigure(0, weight=1, uniform='a')

        #initialize shell container
        self.shell_container_initializer()

        main_frame.MainFrame(self.shell_container)


    def full_screen(self):
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")

    def shell_container_initializer(self):
        self.shell_container = ctk.CTkFrame(self)
        self.shell_container.rowconfigure(0, weight=1, uniform='a')
        self.shell_container.columnconfigure(0, weight=1, uniform='a')
        self.shell_container.grid(column=0, row=0, sticky="nsew")




