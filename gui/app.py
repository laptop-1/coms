import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self, title, dimensions):
        super().__init__()
        self.title(title)
        self.geometry(f"{dimensions[0]}x{dimensions[1]}")

