import tkinter as tk
from tkinter import messagebox

def click_button(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            entry_var.set(result)
            expression = str(result)
        except Exception as e:
            messagebox.showerror("Erreur", "Entrée invalide")
            expression = ""
    elif text == "C":
        expression = ""
        entry_var.set("")
    else:
        expression += text
        entry_var.set(expression)

# Configuration de la fenêtre
expression = ""
root = tk.Tk()
root.title("Calculatrice")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font="Helvetica 20 bold", justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Boutons
buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

frame = tk.Frame(root)
frame.pack()

for i, btn in enumerate(buttons):
    button = tk.Button(frame, text=btn, font="Helvetica 15 bold", width=5, height=2)
    button.grid(row=i//4, column=i%4)
    button.bind("<Button-1>", click_button)

root.mainloop()