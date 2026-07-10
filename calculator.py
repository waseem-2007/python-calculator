import tkinter as tk
window = tk.Tk()
window.title("calculator")
window.geometry("320x500")
window.configure(bg="black")
window.resizable(False, False)
display = tk.Entry(window, width=20, font=("Arial", 24), borderwidth=5, relief="ridge")
display.pack(fill="x", padx=10, pady=10,ipady=20)
def click(value):
    display.insert(tk.END, value)
def clear():
    display.delete(0, tk.END)
def calculate():
    try:
        expression = display.get()
        expression = expression.replace("^", "**")
        expression = expression.replace("÷", "/")
        expression = expression.replace("×", "*")
        expression = expression.replace("%", "/100")
        expression = expression.replace("√", "**0.5")
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

button_frame = tk.Frame(window, bg="black")
button_frame.pack(expand=True, fill="both")
buttons = [
    ["AC", "√", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "^", "="]    
]
for i in range(5):
    button_frame.rowconfigure(i, weight=1)
for j in range(4):
    button_frame.columnconfigure(j, weight=1)   
for row in range(len(buttons)):
    for col in range(len(buttons[row])):
        text = buttons[row][col]
        if text =="AC":
            command = clear
        elif text == "=":
            command = calculate
        else:
            command = lambda value=text: click(value)
        if text in ["+", "-", "×", "÷", "^", "%", "√"]:
            bg="orange"
            fg="white"  
        elif text in ["AC","+/-","%"]:
            bg="gray"
            fg="black"
        else:
            bg="#444444"
            fg="black"
        button = tk.Button(button_frame, text=text, font=("Arial", 18), bg=bg, fg=fg, borderwidth=0, command=command)
        button.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)

window.mainloop()