#A dictionary containing students name and marks
students = {
    "Alice":85,
    "Bob":90,
    "Charlie":93,
    "David":87,
    "Mark":76,
    "Carol":84,
}
#Taking user input
name = input("Enter the name of the student: ").strip().capitalize()

#conditions
if name in students:
    print(f"{name}'s mark : {students[name]}")
else:
    print(f'{name} is not in student list')
