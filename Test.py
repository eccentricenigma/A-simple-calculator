import tkinter as tk

calculation = ""

def add_to(symbol):
    global calculation
    calculation += str(symbol)
    result.delete(1.0, "end")
    result.insert(1.0, calculation)

def _eval():
    global calculation
    try:
        calculation = str(eval(calculation))
        result.delete(1.0, "end")
        result.insert(1.0, calculation)
    except:
        clear()
        result.insert(1.0, "Error")
        
def clear():
    global calculation
    calculation = ""
    result.delete(1.0, "end")


root = tk.Tk()
root.geometry("325x335")

result = tk.Text(root, height = 4, width = 16, font=("Arial, 24"))
result.grid(columnspan=5)

btn_1 = tk.Button(root, text = "1", command = lambda: add_to(1), width = 5, font = ("Arial", 14))     
btn_1.grid(row = 2, column=1)

btn_2 = tk.Button(root, text = "2", command = lambda: add_to(2), width = 5, font = ("Arial", 14))     
btn_2.grid(row = 2, column=2)

btn_3 = tk.Button(root, text = "3", command = lambda: add_to(3), width = 5, font = ("Arial", 14))     
btn_3.grid(row = 2, column=3)

btn_4 = tk.Button(root, text = "4", command = lambda: add_to(4), width = 5, font = ("Arial", 14))     
btn_4.grid(row = 3, column=1)

btn_5 = tk.Button(root, text = "5", command = lambda: add_to(5), width = 5, font = ("Arial", 14))     
btn_5.grid(row = 3, column=2)

btn_6 = tk.Button(root, text = "6", command = lambda: add_to(6), width = 5, font = ("Arial", 14))     
btn_6.grid(row = 3, column=3)

btn_7 = tk.Button(root, text = "7", command = lambda: add_to(7), width = 5, font = ("Arial", 14))     
btn_7.grid(row = 4, column=1)

btn_8 = tk.Button(root, text = "8", command = lambda: add_to(8), width = 5, font = ("Arial", 14))     
btn_8.grid(row = 4, column=2)

btn_9 = tk.Button(root, text = "9", command = lambda: add_to(9), width = 5, font = ("Arial", 14))     
btn_9.grid(row = 4, column=3)

btn_0 = tk.Button(root, text = "0", command = lambda: add_to(0), width = 5, font = ("Arial", 14))     
btn_0.grid(row = 5, column=2)

btn_left = tk.Button(root, text = "(", command = lambda: add_to("("), width = 5, font = ("Arial", 14))     
btn_left.grid(row = 5, column=1)

btn_right = tk.Button(root, text = ")", command = lambda: add_to(")"), width = 5, font = ("Arial", 14))     
btn_right.grid(row = 5, column=3)

btn_add = tk.Button(root, text = "+", command = lambda: add_to("+"), width = 5, font = ("Arial", 14))     
btn_add.grid(row = 2, column=4)

btn_sub = tk.Button(root, text = "-", command = lambda: add_to("-"), width = 5, font = ("Arial", 14))     
btn_sub.grid(row = 3, column=4)

btn_mul = tk.Button(root, text = "x", command = lambda: add_to("*"), width = 5, font = ("Arial", 14))     
btn_mul.grid(row = 4, column=4)

btn_div = tk.Button(root, text = "/", command = lambda: add_to("/"), width = 5, font = ("Arial", 14))     
btn_div.grid(row = 5, column=4)

btn_clr = tk.Button(root, text = "Clear", command = clear, width = 10   , font = ("Arial", 14))     
btn_clr.grid(row = 6, column=1, columnspan=2)

btn_eval = tk.Button(root, text = "=", command = _eval, width = 10, font = ("Arial", 14))     
btn_eval.grid(row = 6, column=3, columnspan=2)
   
root.mainloop()