# Sheridan Dela Cruz
# May 2, 2026
# Module 8.2

# Program loads student JSON, prints list, adds a new student, and updates the file.

import json

# Load the JSON file into a Python list
with open("student.json") as f:
    students = json.load(f)

# Function to print each student in the required format
def print_students(student_list):
    for s in student_list:
        print(f"{s['L_Name']}, {s['F_Name']} : ID = {s['Student_ID']} , Email = {s['Email']}")

# Print original list
print("Original Student List")
print_students(students)

# Append YOUR student info
students.append({
    "F_Name": "Sheridan",
    "L_Name": "Dela Cruz",
    "Student_ID": 121643,
    "Email": "sdc@practice.com"
})

# Print updated list
print("\nUpdated Student List")
print_students(students)

# Write updated list back to JSON file
with open("student.json", "w") as f:
    json.dump(students, f, indent=4)

print("\n.json file updated")