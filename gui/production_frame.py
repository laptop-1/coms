import customtkinter as ctk

class ProductionFrame(ctk.CTkFrame):
    def __init__(self,master, controller):
        super().__init__(master, fg_color="blue")
        self.controller = controller
        #frame positioning
        self.main_frame_griding()
        #frame structuring
        self.main_frame_partitioning()

    def main_frame_griding(self):
        self.grid(column=0, row=0, sticky="nsew")

    def main_frame_partitioning(self):
        self.rowconfigure(0, weight=1, uniform='a')
        self.rowconfigure((1,2), weight=2, uniform='a')
        self.columnconfigure(0, weight=1,uniform='a')
        self.columnconfigure(1, weight=2, uniform='a')
        self.columnconfigure(2, weight=1, uniform='a')

