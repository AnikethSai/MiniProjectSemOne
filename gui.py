import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("Simplfied Expense Tracker")
        
        # add widgets to app
        #self.button = customtkinter.CTkButton(self, command=self.button_click, corner_radius=32, fg_color = "transparent", hover_color="#4158D0", border_color = "#FFCC70",border_width=2)
        
        #self.button.grid(row=0, column=0, padx=20, pady=10)
        # Configure grid layout for centering 
        #self.button.place(relx = 0.5, rely = 0.5, anchor = "center")
        
        # Add an Entry widget for user input 
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter Number of people", width=300) 
        self.entry.grid(row=10, column=10, padx=0, pady=0, sticky="nsew") 
        self.entry.place(relx = 0.5, rely = 0.5, anchor = "center")
        #  Add a button widget to trigger the input read 
        self.button = customtkinter.CTkButton(self, text="Submit", command=self.button_click,corner_radius=32, fg_color = "transparent", hover_color="#4158D0", border_color = "#FFCC70",border_width=2) 
        self.button.grid(row=500, column=1000, padx=0, pady=0, sticky="nsew")
        self.button.place(relx = 0.5, rely = 0.6, anchor = "center")
       
    # add methods to app
    def button_click(self):
        user_input = self.entry.get()
        print(f"The number of people:, {user_input}!")
        


app = App()
app.mainloop()