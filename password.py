import tkinter as tk
from tkinter import messagebox
import random
import math

alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "@#$%&*"

def generate_password(pass_len):
    alpha_len = pass_len // 2
    num_len = math.ceil(pass_len * 30 / 100)
    special_len = pass_len - (alpha_len + num_len)

    password = []

    def generate_pass(length, array, is_alpha=False):
        for i in range(length):
            character = array[random.randint(0, len(array) - 1)]
            if is_alpha:
                character = character.upper() if random.randint(0, 1) == 1 else character
            password.append(character)

    generate_pass(alpha_len, alpha, True)
    generate_pass(num_len, num)
    generate_pass(special_len, special)
    random.shuffle(password)

    return "".join(password)

def on_generate_clicked():
    try:
        pass_len = int(pass_len_var.get())
        if pass_len < 8:
            messagebox.showerror("Error", "Password length must be at least 8 characters.")
            return
        password_display_var.set(generate_password(pass_len))
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_display_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")

pass_len_var = tk.StringVar()
password_display_var = tk.StringVar()

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

tk.Label(frame, text="Enter Password Length:", fg="blue").pack()
tk.Entry(frame, textvariable=pass_len_var, bg="#FFF2CC").pack()

tk.Button(frame, text="Generate Password", command=on_generate_clicked, bg="#C2DFFF").pack(pady=5)
tk.Label(frame, textvariable=password_display_var, bg="white", width=20, relief="sunken").pack(pady=5)
tk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard, bg="#D5E8D4").pack(pady=5)

root.mainloop()
