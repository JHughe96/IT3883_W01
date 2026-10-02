# Program Name: Assignment1.py
# Course: IT3883/Section W01
# Student Name: Jason Hughes
# Assignment Number: 1
# Due Date: 09/01/ 2026
# Purpose: This program is to manipulate a buffer string
# List Specific resources used to complete the assignment.

# Varibles
buffer = ""

while True:
    
# Get user input
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit program")
    selection = input("Enter option 1-4.")


# Perform operation from input
    if selection == "1":
        append = input("Enter string to append: ")
        buffer += append
        print("Data added")

    elif selection == "2":
        buffer = ""
        print("Data cleared")

    elif selection == "3":
        print(buffer)

    elif selction == "4":
        print("Goodbye")
        break

# Handle invalid inputs
    else:
        print("Invalid, please chooose 1 through 4")
    
