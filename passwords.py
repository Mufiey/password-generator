import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    character_sets = []
    if use_upper:
        character_sets.append(string.ascii_uppercase)
    if use_lower:
        character_sets.append(string.ascii_lowercase)
    if use_digits:
        character_sets.append(string.digits)
    if use_special:
        character_sets.append(string.punctuation)

    if not character_sets:
        return None

    password_chars = [random.choice(char_set) for char_set in character_sets]
    all_chars = "".join(character_sets)
    password_chars += [random.choice(all_chars) for _ in range(length - len(password_chars))]
    random.shuffle(password_chars)
    return "".join(password_chars)

def on_generate():
    try:
        length = int(entry_length.get())
        if length < 6:
            messagebox.showerror("Error", "Password length must be at least 6.")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        return

    use_upper = var_upper.get()
    use_lower = var_lower.get()
    use_digits = var_digits.get()
    use_special = var_special.get()

    if not (use_upper or use_lower or use_digits or use_special):
        messagebox.showerror("Error", "You must select at least one character type!")
        return

    password = generate_password(length, use_upper, use_lower, use_digits, use_special)
    if password:
        text_password.delete(0, tk.END)
        text_password.insert(0, password)
    else:
        messagebox.showerror("Error", "Failed to generate password.")

def copy_password():
    password = text_password.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy.")
        
root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Password length (min 6):").grid(row=0, column=0, sticky="w")
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1)
entry_length.insert(0, "12")

var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_special = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Uppercase letters", variable=var_upper).grid(row=1, column=0, sticky="w")
tk.Checkbutton(root, text="Lowercase letters", variable=var_lower).grid(row=1, column=1, sticky="w")
tk.Checkbutton(root, text="Digits", variable=var_digits).grid(row=2, column=0, sticky="w")
tk.Checkbutton(root, text="Special Characters ", variable=var_special).grid(row=2, column=1, sticky="w")

btn_generate = tk.Button(root, text="Generate password", command=on_generate)
btn_generate.grid(row=3, column=0, columnspan=2, pady=10)

tk.Label(root, text="Generated password:").grid(row=4, column=0, sticky="w")
text_password = tk.Entry(root, width=40)
text_password.grid(row=4, column=1)

btn_copy = tk.Button(root, text="Copy password", command=copy_password)
btn_copy.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()
