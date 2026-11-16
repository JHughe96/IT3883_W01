# Program Name: Assignment_5.py
# Course: IT3883/Section W01
# Student Name: Jason Hughes
# Assignment Number: Assignment_5
# Due Date: 11/20/2026
# Purpose: Program to display average temprature
# List specific resources used to complete the assignment: 

import sqlite3
from pathlib import Path


def main():
    # Find the data file in the same folder.
    input_path = Path(__file__).with_name("Assignment5input.txt")
    database_path = Path(__file__).with_name("Assignment5.db")

    if not input_path.is_file():
        print(f"Input file not found: {input_path}")
        return

    # Connect to SQLite and create the temperature table.
    with sqlite3.connect(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Temperatures (
                ID INTEGER PRIMARY KEY,
                Day_Of_Week TEXT NOT NULL,
                Temperature_Value REAL NOT NULL
            )
        """)

        # Remove old readings so running the program twice doesn't duplicate data.
        cursor.execute("DELETE FROM Temperatures")

        # Parse each line, checking that it has a weekday and numeric reading.
        with input_path.open("r", encoding="utf-8") as input_file:
            for line_number, line in enumerate(input_file, start=1):
                parts = line.strip().split()
                if not parts:
                    continue
                if len(parts) != 2:
                    raise ValueError(f"Invalid data on line {line_number}: {line.strip()}")

                day_of_week, temperature_text = parts
                temperature_value = float(temperature_text)
                cursor.execute(
                    "INSERT INTO Temperatures (Day_Of_Week, Temperature_Value) VALUES (?, ?)",
                    (day_of_week, temperature_value),
                )

        # Use SQL AVG to calculate the temperature for each requested day.
        for day in ("Sunday", "Thursday"):
            cursor.execute(
                "SELECT AVG(Temperature_Value) FROM Temperatures WHERE Day_Of_Week = ?",
                (day,),
            )
            average = cursor.fetchone()[0]
            if average is None:
                print(f"No temperature readings found for {day}.")
            else:
                print(f"Average temperature for {day}: {average:.2f}")


if __name__ == "__main__":
    main()
