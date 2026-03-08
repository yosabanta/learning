# Tutedude Assignment 5
## Module 6: Data Structures and Strings in Python

This assignment demonstrates the use of Python **dictionaries**, **lists**, and **list slicing**.

---

## Task 1: Create a Dictionary of Student Marks

### Description
A dictionary is created where student names are keys and their marks are values.

The program:
- Prompts the user to enter a student's name.
- Uses `strip()` to remove extra spaces.
- Uses `capitalize()` to standardize the name format.
- Checks whether the student exists in the dictionary.
- Displays the student's marks if found.
- Displays an appropriate message if the student is not found.

### File
task1_student_marks.py

### Example
Enter the name of the student: Alice  
Alice's mark : 85

If the student does not exist:

Enter the name of the student: John  
John is not in student list

---

## Task 2: Demonstrate List Slicing

### Description
A list of numbers from **1 to 10** is created.

The program:
- Extracts the **first five elements** from the list using slicing.
- Reverses the extracted elements.
- Prints the original list, the sliced list, and the reversed list.

### File
task2_list_slicing.py

### Example Output
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
Sliced list: [1, 2, 3, 4, 5]  
Reversed list: [5, 4, 3, 2, 1]

---

## Concepts Used
- Dictionaries
- Lists
- List slicing
- String methods (`strip()`, `capitalize()`)
- Conditional statements
- Python data structures

---

## How to Run

Run Task 1:
python task1_student_marks.py

Run Task 2:
python task2_list_slicing.py