# Program Name: Assignment3.py
# Course: IT3883/Section W01
# Student Name: Jason Hughes
# Assignment Number: Assignment3
# Due Date: 10/12/2026
# Purpose: Program to find miles per gallon
# List specific resources used to complete the assignment: 

from tkinter import *

# This function runs when the user changes the MPG entry box.
def convert_mpg(*args):
    # Get the text entered by the user
    user_input = mpg_input.get()

    # If the box is empty, clear the result instead of causing an error
    if user_input == "":
        result.set("")
        return

    try:
        # Convert the user's entry into a float number
        mpg = float(user_input)

        # Convert miles per gallon to kilometers per liter with formula
        # 1 mpg = 0.425143707 km/l
        km_per_liter = mpg * 0.425143707

        # Display the result rounded to 4 decimal places
        result.set(format(km_per_liter, ".4f"))

    except ValueError:
        # If the user types a letter or other invalid value,
        # display error message instead of crashing
        result.set("Invalid input")


# Create the main GUI window
root = Tk()

# Set the window title and size
root.title("MPG to KM/L Converter")
root.geometry("350x180")

# Create a heading label
title_label = Label(
    root,
    text="Miles per Gallon to Kilometers per Liter",
    font=("Arial", 12, "bold")
)
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=15)

# Create labels for the input and output
mpg_label = Label(root, text="Miles per Gallon (MPG):")
mpg_label.grid(row=1, column=0, padx=10, pady=5)

result_label = Label(root, text="Kilometers per Liter (KM/L):")
result_label.grid(row=2, column=0, padx=10, pady=5)

# StringVar stores the user's MPG entry
mpg_input = StringVar()

# StringVar stores the converted answer
result = StringVar()

# Create the input box
mpg_entry = Entry(root, textvariable=mpg_input, width=15)
mpg_entry.grid(row=1, column=1, padx=10, pady=5)

# Create a label that displays the conversion result
output_label = Label(
    root,
    textvariable=result,
    width=15,
    bg="white",
    relief="sunken"
)
output_label.grid(row=2, column=1, padx=10, pady=5)

# Watch the input variable for changes.
# Each time the user types or deletes a character,
# the convert_mpg function runs automatically.
mpg_input.trace_add("write", convert_mpg)

# Put the cursor in the input box when the program starts
mpg_entry.focus()

# Start the Tkinter event loop
root.mainloop()
