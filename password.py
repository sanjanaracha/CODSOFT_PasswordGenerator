import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

def generate_password(length, complexity):
    if complexity == 1:
        characters = string.ascii_lowercase
    elif complexity == 2:
        characters = string.ascii_letters
    elif complexity == 3:
        characters = string.ascii_letters + string.digits
    elif complexity == 4:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate():
    try:
        length = int(length_var.get())
        if length <= 0:
            messagebox.showerror("Invalid Input", "Password length must be a positive integer.")
            return
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for length.")
        return

    complexity = complexity_var.get()
    password = generate_password(length, complexity)
    if password:
        result_var.set(password)
        messagebox.showinfo("Generated Password", f"Your generated password is:\n{password}")
    else:
        messagebox.showerror("Invalid Input", "Invalid complexity level selected.")

app = tk.Tk()
app.title("Password Generator")
app.geometry("600x450")
app.configure(bg='orange')

style = ttk.Style()
style.configure('Orange.TFrame', background='orange')

frame = ttk.Frame(app, padding=50, style='Orange.TFrame')
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Length of the Password:",background="#5E65EE").grid(row=0, column=0, sticky=tk.W)
length_var = tk.StringVar()
length_entry = ttk.Entry(frame, textvariable=length_var)
length_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Level of Complexity:",background="#5E65EE").grid(row=1, column=0, sticky=tk.W)
complexity_var = tk.IntVar(value=1)
complexity_frame = ttk.Frame(frame)
complexity_frame.grid(row=1, column=1, sticky=tk.W)

ttk.Radiobutton(complexity_frame, text="1 - Lowercase letters only", variable=complexity_var, value=1).grid(row=0, column=0, sticky=tk.W)
ttk.Radiobutton(complexity_frame, text="2 - Lowercase and Uppercase letters", variable=complexity_var, value=2).grid(row=1, column=0, sticky=tk.W)
ttk.Radiobutton(complexity_frame, text="3 - Letters and Numbers", variable=complexity_var, value=3).grid(row=2, column=0, sticky=tk.W)
ttk.Radiobutton(complexity_frame, text="4 - Letters, Numbers, and Symbols", variable=complexity_var, value=4).grid(row=3, column=0, sticky=tk.W)

generate_button = ttk.Button(frame, text="Generate Password", command=on_generate)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

ttk.Label(frame, text="Generated Password:",background="#5E65EE").grid(row=3, column=0, sticky=tk.W)
result_var = tk.StringVar()
result_entry = ttk.Entry(frame, textvariable=result_var, state="readonly", width=40)
result_entry.grid(row=3, column=1, sticky=(tk.W, tk.E))

app.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

app.mainloop()