import tkinter as tk
from tkinter import PhotoImage
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("650x540")
        
        self.background_image = PhotoImage(file="password-generator.png")

        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)


        self.label_name = tk.Label(root, text="Enter Your Name:")
        self.label_name.pack()

        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.label_length = tk.Label(root, text="Enter Password Length:")
        self.label_length.pack()

        self.length_entry = tk.Entry(root)
        self.length_entry.pack()

        self.lowercase_var = tk.BooleanVar()
        self.lowercase_check = tk.Checkbutton(root, text="Include Lowercase", variable=self.lowercase_var)
        self.lowercase_check.pack()

        self.uppercase_var = tk.BooleanVar()
        self.uppercase_check = tk.Checkbutton(root, text="Include Uppercase", variable=self.uppercase_var)
        self.uppercase_check.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
        self.result_label = tk.Label(root, text="", fg="red", font=("Helvetica", 15, "bold"))
        self.result_label.place(x=50, y=400, width=500, height=70)

    def generate_password(self):
        name = self.name_entry.get()
        password_length = int(self.length_entry.get())
        include_lowercase = self.lowercase_var.get()
        include_uppercase = self.uppercase_var.get()

        characters = ""
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_uppercase:
            characters += string.ascii_uppercase
        characters += string.digits + string.punctuation

        if not characters:
            self.result_label.config(text="Select at least one character type")
            return

        password = ''.join(random.choice(characters) for _ in range(password_length))
        self.result_label.config(text=f"Password for {name}: {password}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
