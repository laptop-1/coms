from random import uniform

import customtkinter as ctk

class MainFrame(ctk.CTkFrame):
    def __init__(self,master,controller):
        super().__init__(master, fg_color="white")
        self.controller = controller

        #frame positioning
        self.main_frame_griding()
        #frame structuring
        self.main_frame_partitioning()
        #gui elements creation
        self.gui_elements_creation()
        #gui elements positioning
        self.gui_elements_positoning()


    def main_frame_griding(self):
        self.grid(column=0, row=0, sticky="nsew")

    def main_frame_partitioning(self):
        self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')
        self.columnconfigure((0, 1, 2), weight=1, uniform='a')

    def gui_elements_creation(self):
        self.main_frame_lable = ctk.CTkLabel(self,text="Customer Order Management", font=("Arial", 30,"bold"))
        self.customer_button = ctk.CTkButton(self,text="Customer", font=("Arial", 25,"bold"))
        self.order_button = ctk.CTkButton(self, text="Order", font=("Arial", 25,"bold"))
        self.production_button = ctk.CTkButton(self, text="Production", font=("Arial", 25,"bold"), command=lambda :self.customer_screen_calling())
        self.delivery_button = ctk.CTkButton(self, text="Delivery", font=("Arial", 25,"bold"))

    def gui_elements_positoning(self):
        self.main_frame_lable.grid(column=1,row=0, sticky="nsew")
        self.customer_button.grid(column=1,row=1,sticky="nsew", pady=5)
        self.order_button.grid(column=1,row=2,sticky="nsew", pady=5)
        self.production_button.grid(column=1,row=3,sticky="nsew", pady=5)
        self.delivery_button.grid(column=1,row=4,sticky="nsew", pady=5)

    def customer_screen_calling(self):
        self.controller.display_screen(self.controller.screen_list[1])

