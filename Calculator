from tkinter import *

# Create the main window
root = Tk()
root.title("Simple Arithmetic Calculator")
root.geometry('300x220')
root.resizable(False, False)

# Function to perform calculation
def perform_calculation():
    try:
        val1 = float(input1.get())
        val2 = float(input2.get())
    except ValueError:
        result_output.config(text="Please enter valid numbers.")
        return

    op = selected_operator.get()

    if op == "+":
        result = val1 + val2
    elif op == "-":
        result = val1 - val2
    elif op == "*":
        result = val1 * val2
    elif op == "/":
        if val2 == 0:
            result_output.config(text="Cannot divide by zero.")
            return
        result = val1 / val2
    else:
        result_output.config(text="Please select an operation.")
        return

    result_output.config(text=f"Result: {result}")

# First number input
label_num1 = Label(root, text="First Number:")
label_num1.grid(row=0, column=0, padx=10, pady=5)
input1 = Entry(root)
input1.grid(row=0, column=1, padx=10, pady=5)

# Second number input
label_num2 = Label(root, text="Second Number:")
label_num2.grid(row=1, column=0, padx=10, pady=5)
input2 = Entry(root)
input2.grid(row=1, column=1, padx=10, pady=5)

# Operation selection
selected_operator = StringVar(value="+")

label_operator = Label(root, text="Choose Operation:")
label_operator.grid(row=2, column=0, padx=10, pady=5)

operator_frame = Frame(root)
operator_frame.grid(row=2, column=1, padx=10, pady=5)

for symbol in ["+", "-", "*", "/"]:
    Radiobutton(operator_frame, text=symbol, variable=selected_operator, value=symbol).pack(side=LEFT)

# Calculate button
calc_button = Button(root, text="Calculate", command=perform_calculation, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
calc_button.grid(row=3, column=0, columnspan=2, pady=10)

# Result display
result_output = Label(root, text="Result will appear here", fg="blue", font=("Arial", 11))
result_output.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()
