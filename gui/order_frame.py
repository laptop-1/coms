import customtkinter as ctk

class OrderFrame(ctk.CTkFrame):
    def __init__(self,master, controller):
        super().__init__(master, fg_color="green")
        self.controller = controller
        #frame positioning
        self.main_frame_griding()
        #frame structuring
        self.main_frame_partitioning()

    def main_frame_griding(self):
        self.grid(column=0, row=0, sticky="nsew")

    def main_frame_partitioning(self):
        pass

