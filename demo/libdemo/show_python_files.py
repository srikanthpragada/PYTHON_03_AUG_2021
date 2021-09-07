import os


def showfile(filename):
    print(f"{'*' * 10} {filename} {'*' * 10}")

    with open(filename, "rt") as f:
        for (lineno, line) in enumerate(f.readlines(), start=1):
            print(f"{lineno:3}: {line}", end='')

    print('-' * 80 + "\n")


allfiles = os.walk(r"c:\classroom\aug3\demo")
count = 0
for (dirname, dirs, files) in allfiles:
    for f in files:
        if f.endswith(".py"):
            showfile(dirname + "\\" + f)
            count += 1

print(f"Count = {count}")
