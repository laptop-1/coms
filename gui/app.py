import customtkinter as ctk
from . import main_frame
from . import customer_frame
from . import order_frame
from . import production_frame

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

        self.initialize_all_screen()

        self.display_default_screen(self.screen_dict["main"])


    def full_screen(self):
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")

    def shell_container_initializer(self):
        self.shell_container = ctk.CTkFrame(self)
        self.shell_container.rowconfigure(0, weight=1, uniform='a')
        self.shell_container.columnconfigure(0, weight=1, uniform='a')
        self.shell_container.grid(column=0, row=0, sticky="nsew")

    def initialize_all_screen(self):
        self.screen_dict = {}
        main_frame_screen = main_frame.MainFrame(self.shell_container, self)
        customer_frame_screen = customer_frame.CustomerFrame(self.shell_container, self)
        order_frame_screen = order_frame.OrderFrame(self.shell_container, self)
        production_frame_screen = production_frame.ProductionFrame(self.shell_container, self)
        self.screen_dict["main"] = main_frame_screen
        self.screen_dict["customer"] = customer_frame_screen
        self.screen_dict["order"] = order_frame_screen
        self.screen_dict["production"] = production_frame_screen

    def display_screen(self,screen_object):
        screen_object.tkraise()

    def display_default_screen(self,screen_object):
        self.display_screen(screen_object)



