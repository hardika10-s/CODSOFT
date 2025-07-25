import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        total_length = int(entry_total.get())
        num_letters = int(entry_letters.get())
        num_digits = int(entry_digits.get())
        num_specials = int(entry_specials.get())

        if num_letters + num_digits + num_specials > total_length:
            messagebox.showerror("Error", "Sum of letters, digits and special characters exceeds total length.")
            return

        letters = random.choices(string.ascii_letters, k=num_letters)
        digits = random.choices(string.digits, k=num_digits)
        specials = random.choices("!@#$%^&*()", k=num_specials)
        remaining = total_length - (num_letters + num_digits + num_specials)
        others = random.choices(string.ascii_letters + string.digits + "!@#$%^&*()", k=remaining)

        password_list = letters + digits + specials + others
        random.shuffle(password_list)
        password = ''.join(password_list)

        entry_result.config(state='normal')
        entry_result.delete(0, tk.END)
        entry_result.insert(0, password)
        entry_result.config(state='readonly')
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers only.")

root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="Total Password Length:").pack(pady=5)
entry_total = tk.Entry(root)
entry_total.pack()

tk.Label(root, text="Number of Letters:").pack(pady=5)
entry_letters = tk.Entry(root)
entry_letters.pack()

tk.Label(root, text="Number of Digits:").pack(pady=5)
entry_digits = tk.Entry(root)
entry_digits.pack()

tk.Label(root, text="Number of Special Characters:").pack(pady=5)
entry_specials = tk.Entry(root)
entry_specials.pack()

tk.Button(root, text="Generate Password", command=generate_password, bg="#007ACC", fg="white").pack(pady=15)

tk.Label(root, text="Your Password:").pack()
entry_result = tk.Entry(root, width=40, state='readonly', justify='center')
entry_result.pack(pady=5)

root.mainloop()
