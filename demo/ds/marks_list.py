data = ["Steve,85", "Mike,56", "Andy,90", "Bob,70", "Richards,87", "Mike,90"]

students = {}

for entry in data:
    name, marks = entry.split(",")
    students[name] = marks

for name, marks in sorted(students.items()):
    print(f"{name:10} {marks:3}")
