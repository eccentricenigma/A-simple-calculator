import customtkinter

calculation = ""
#t
class Calc(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
        
        

        def add_to(symbol):
            global calculation
            calculation += str(symbol)
            self.result.delete(1.0, "end")
            self.result.insert(1.0, calculation)

        def _eval():
            global calculation
            try:
                calculation = str(eval(calculation))
                self.result.delete(1.0, "end")
                self.result.insert(1.0, calculation)
            except:
                clear()
                self.result.insert(1.0, "Error")
                
        def clear():
            global calculation
            calculation = ""
            self.result.delete(1.0, "end")

        self.grid_rowconfigure(0, weight=3)
        
        self.result = customtkinter.CTkTextbox(master=self,
                                    font = customtkinter.CTkFont(family = "Arial", size = 24))
        self.result.grid(row = 0, column = 0, rowspan = 3, columnspan=5, pady = (0,20), sticky="nsew")

        # Use CTkButton instead of tkinter Button
        self.button1 = customtkinter.CTkButton(master=self, 
                                        width=100,
                                        height=50,
                                        font = customtkinter.CTkFont(family = "Arial", size = 14), 
                                        text="1", 
                                        border_width = 1,
                                        corner_radius = 2,
                                        command = lambda: add_to(1))
        self.button1.grid(row = 3, column = 1, padx = 2, pady = 2)

        self.button2 = customtkinter.CTkButton(master=self, 
                                        width=100,
                                        height=50,
                                        font = customtkinter.CTkFont(family = "Arial", size = 14), 
                                        text="2", 
                                        border_width = 1,
                                        corner_radius = 2,
                                        command = lambda: add_to(2))
        self.button2.grid(row = 3, column = 2, padx = 2, pady = 2)

        self.button3 = customtkinter.CTkButton(master=self, 
                                        width=100,
                                        height=50,
                                        font = customtkinter.CTkFont(family = "Arial", size = 14), 
                                        text="3", 
                                        border_width = 1,
                                        corner_radius = 2,
                                        command = lambda: add_to(3))
        self.button3.grid(row = 3, column = 3, padx = 2, pady = 2)

        self.button4 = customtkinter.CTkButton(master=self, 
                                        width=100,
                                        height=50,
                                        font = customtkinter.CTkFont(family = "Arial", size = 14), 
                                        text="4", 
                                        border_width = 1,
                                        corner_radius = 2,
                                        command = lambda: add_to(4))
        self.button4.grid(row = 4, column = 1, padx = 2, pady = 2)

        self.button5 = customtkinter.CTkButton(master=self, 
                                        width=100,
                                        height=50,
                                        font = customtkinter.CTkFont(family = "Arial", size = 14), 
                                        text="5", 
                                        border_width = 1,
                                        corner_radius = 2,
                                        command = lambda: add_to(5))
        self.button5.grid(row = 4, column = 2, padx = 2, pady = 2)

        self.button6 = customtkinter.CTkButton(master=self, 
                                        width=100,
                                        height=50,
                                        font = customtkinter.CTkFont(family = "Arial", size = 14), 
                                        text="6", 
                                        border_width = 1,
                                        corner_radius = 2,
                                        command = lambda: add_to(6))
        self.button6.grid(row = 4, column = 3, padx = 2, pady = 2)

        self.button7 = customtkinter.CTkButton(master=self, 
                                        width=100,
                                        height=50,
                                        font = customtkinter.CTkFont(family = "Arial", size = 14), 
                                        text="7", 
                                        border_width = 1,
                                        corner_radius = 2,
                                        command = lambda: add_to(7))
        self.button7.grid(row = 5, column = 1, padx = 2, pady = 2)

        self.button8 = customtkinter.CTkButton(master=self, 
                                        width=100,
                                        height=50,
                                        font = customtkinter.CTkFont(family = "Arial", size = 14), 
                                        text="8", 
                                        border_width = 1,
                                        corner_radius = 2,
                                        command = lambda: add_to(8))
        self.button8.grid(row = 5, column = 2, padx = 2, pady = 2)

        self.button9 = customtkinter.CTkButton(master=self, 
                                        width=100,
                                        height=50,
                                        font = customtkinter.CTkFont(family = "Arial", size = 14), 
                                        text="9", 
                                        border_width = 1,
                                        corner_radius = 2,
                                        command = lambda: add_to(9))
        self.button9.grid(row = 5, column = 3, padx = 2, pady = 2)

        self.button0 = customtkinter.CTkButton(master=self, 
                                        width=100,
                                        height=50,
                                        font = customtkinter.CTkFont(family = "Arial", size = 14), 
                                        text="0", 
                                        border_width = 1,
                                        corner_radius = 2,
                                        command = lambda: add_to(0))
        self.button0.grid(row = 6, column = 2, padx = 2, pady = 2)
                
        self.button_add = customtkinter.CTkButton(master=self, 
                                        width=100,
                                        height=50,
                                        font = customtkinter.CTkFont(family = "Arial", size = 14), 
                                        text="+", 
                                        border_width = 1,
                                        corner_radius = 2,
                                        command = lambda: add_to("+"))
        self.button_add.grid(row = 3, column = 4, padx = 2, pady = 2)

        self.button_sub = customtkinter.CTkButton(master=self, 
                                        width=100,
                                        height=50,
                                        font = customtkinter.CTkFont(family = "Arial", size = 14), 
                                        text="-", 
                                        border_width = 1,
                                        corner_radius = 2,
                                        command = lambda: add_to("-"))
        self.button_sub.grid(row = 4, column = 4, padx = 2, pady = 2)

        self.button_mul = customtkinter.CTkButton(master=self, 
                                        width=100,
                                        height=50,
                                        font = customtkinter.CTkFont(family = "Arial", size = 14), 
                                        text="x", 
                                        border_width = 1,
                                        corner_radius = 2,
                                        command = lambda: add_to("*"))
        self.button_mul.grid(row = 5, column = 4, padx = 2, pady = 2)

        self.button_div = customtkinter.CTkButton(master=self, 
                                        width=100,
                                        height=50,
                                        font = customtkinter.CTkFont(family = "Arial", size = 14), 
                                        text="/", 
                                        border_width = 1,
                                        corner_radius = 2,
                                        command = lambda: add_to("/"))
        self.button_div.grid(row = 6, column = 4, padx = 2, pady = 2)

        self.button_right = customtkinter.CTkButton(master=self, 
                                        width=100,
                                        height=50,
                                        font = customtkinter.CTkFont(family = "Arial", size = 14), 
                                        text=")", 
                                        border_width = 1,
                                        corner_radius = 2,
                                        command = lambda: add_to(")"))
        self.button_right.grid(row = 6, column = 3, padx = 2, pady = 2)

        self.button_left = customtkinter.CTkButton(master=self, 
                                        width=100,
                                        height=50,
                                        font = customtkinter.CTkFont(family = "Arial", size = 14), 
                                        text="(", 
                                        border_width = 1,
                                        corner_radius = 2,
                                        command = lambda: add_to("("))
        self.button_left.grid(row = 6, column = 1, padx = 2, pady = 2)

        self.button_clear = customtkinter.CTkButton(master=self, 
                                        width=100,
                                        height=50,
                                        font = customtkinter.CTkFont(family = "Arial", size = 14), 
                                        text="Clear", 
                                        border_width = 1,
                                        corner_radius = 2,
                                        command = clear)
        self.button_clear.grid(row = 7, column = 1,columnspan=2, padx = 2, pady = 2, sticky = "nsew")

        self.button_eval = customtkinter.CTkButton(master=self, 
                                        width=100,
                                        height=50,
                                        font = customtkinter.CTkFont(family = "Arial", size = 14), 
                                        text="=", 
                                        border_width = 1,
                                        corner_radius = 2,
                                        command = _eval)
        self.button_eval.grid(row = 7, column = 3, columnspan=2, padx = 2, pady = 2, sticky = "nsew")        
        
if __name__ == "__main__":
    self= Calc()
    self.mainloop()