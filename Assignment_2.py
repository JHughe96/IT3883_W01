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

    for line in file:
        line = line.strip()

        # Skip blank lines
        if line == "":
            continue

        # Split the line using the tab delimiter
        data = line.split("\t")


        # Store name
        name = data[0]

        # Get grade data into Int
        scores = []
        for score in data[1:]:
            scores.append(int(score))

            # Find average
            average = sum(scores) / len(scores)

            # Store the name with average for student
            students.append([name, average])

        # Sort students by average in descending order
        students.sort(key=lambda student: student[1], reverse=True)

        # Display results
        for student in students:
            print(student[0], format(student[1], ".2f"))

            

