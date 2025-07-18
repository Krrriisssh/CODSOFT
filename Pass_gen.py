from tkinter import *
import random
import string

# Create the main window
root = Tk()
root.title("Simple Password Generator")
root.geometry('400x220')
root.resizable(False, False)

# Label for password length
length_label = Label(root, text="Enter password length:", font=("Arial", 12))
length_label.place(x=10, y=20)

# Entry box for user to enter password length
length_input = Entry(root, width=5, font=("Arial", 12))
length_input.place(x=200, y=20)

# Label to display the generated password
output_label = Label(root, text="", font=("Arial", 12), fg="blue", wraplength=380, justify=LEFT)
output_label.place(x=10, y=120)

# Function to create a random password
def generate_password():
    try:
        pwd_length = int(length_input.get())
        if pwd_length < 5:
            output_label.config(text="Please use at least 5 characters.")
        else:
            all_chars = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choices(all_chars, k=pwd_length))
            output_label.config(text="Your Password: " + password)
    except ValueError:
        output_label.config(text="Invalid input. Please enter a number.")

# Button to trigger password generation
generate_btn = Button(root, text="Generate", command=generate_password, bg="#2196F3", fg="white", font=("Arial", 11, "bold"))
generate_btn.place(x=150, y=70)

root.mainloop()
