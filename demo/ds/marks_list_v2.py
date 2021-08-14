data = ["Steve,85", "Mike,56", "Mike,80", "Bob,89", "Andy:89",
        "Steve,75", "Andy,90", "Bob,70", "Richards,87", "Mike,90"]

students = {}

for entry in data:
    values = entry.split(",")
    if len(values) < 2:
        continue

    name = values[0]
    marks = int(values[1])
    if name in students:
        students[name] = students[name] + marks
    else:
        students[name] = marks

for name, marks in sorted(students.items()):
    print(f"{name:10} {marks:3}")
