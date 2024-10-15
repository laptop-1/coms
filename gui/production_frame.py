import customtkinter as ctk

class ProductionFrame(ctk.CTkFrame):
    def __init__(self,master, controller):
        super().__init__(master)
        self.controller = controller
        #frame positioning
        self.main_frame_griding()
        #frame structuring
        self.main_frame_partitioning()

        self.gui_elements_creation()

        self.gui_elements_positioning()

    def main_frame_griding(self):
        self.grid(column=0, row=0, sticky="nsew")

    def main_frame_partitioning(self):
        self.rowconfigure(0, weight=1, uniform='a')
        self.rowconfigure((1,2), weight=2, uniform='a')
        self.columnconfigure(0, weight=1,uniform='a')
        self.columnconfigure(1, weight=2, uniform='a')
        self.columnconfigure(2, weight=1, uniform='a')

    #creation of the gui elements
    def gui_elements_creation(self):
        self.back_button = ctk.CTkButton(self,text="Back", font=("Arial", 20, "bold"))
        self.title_label = ctk.CTkLabel(self, text="Production", font=("Arial", 20, "bold"))
        self.today_production_date_button = ctk.CTkButton(self, text="Same Production Report", font=("Arial", 20, "bold"), width=100,height=50)
        self.specific_day_frame_creation()

    #creation for the specific day wigets inside the frame
    def specific_day_frame_creation(self):
        #frame creation and gridding
        self.specific_day_frame = ctk.CTkFrame(self)
        self.specific_day_frame.rowconfigure(0,weight=1, uniform='a')
        self.specific_day_frame.rowconfigure(1,weight=2, uniform='a')
        self.specific_day_frame.rowconfigure(2,weight=2, uniform='a')
        self.specific_day_frame.columnconfigure((0,1,2), weight=1, uniform='a')

        #gui specific day elements creation
        self.specific_day_production_report_label = ctk.CTkLabel(self.specific_day_frame, text="Specific Day Production Report", fg_color="green")
        self.entry_date_label = ctk.CTkLabel(self.specific_day_frame, text="Enter Date", fg_color="green")
        self.specific_day_entry = ctk.CTkEntry(self.specific_day_frame, fg_color="green")
        self.export_button = ctk.CTkButton(self.specific_day_frame, text="Export", fg_color="green")

        #gui specific day griding
        self.specific_day_production_report_label.grid(row=0, column=1, sticky="nsew")
        self.entry_date_label.grid(row=1, column=0, sticky="e")
        self.specific_day_entry.grid(row=1, column=1)
        self.export_button.grid(row=2,column=1, sticky="n")



    #position the elements on the gui
    def gui_elements_positioning(self):
        self.back_button.grid(column=0, row=0)
        self.title_label.grid(column=1, row=0, sticky="nsew")
        self.today_production_date_button.grid(column=1, row=1)
        self.specific_day_frame.grid(column=1, row=2, sticky="nsew")






