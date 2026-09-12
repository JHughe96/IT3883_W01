# Program Name: Assignment2.py
# Course: IT3883/Section W01
# Student Name: Jason Hughes
# Assignment Number: Assignment2
# Due Date: 09/12/2026
# Purpose: Program to find students average then display in order
# List specific resources used to complete the assignment: 

# Define students varable
students = []

# Open file
with open("Assign2input.txt", "r") as file:

    # Break data into parts
    for line in file:
        data = line.strip()
        data = data.split()

        # Store name
        name = data[0]

        # Get grade data into Integers
        scores = []
        for score in data[1:]:
            scores.append(int(score))

        # Find average
        average = sum(scores) / len(scores)

        # Store the name with average for student together
        students.append([name, average])

    # Sort students by average in descending order
    students.sort(key=lambda student: student[1], reverse=True)

    # Display results
    for student in students:
        print(student[0], format(student[1], ".2f"))

    # Keep window open for results to be viewed if needed
    input("Press ENTER to exit")
