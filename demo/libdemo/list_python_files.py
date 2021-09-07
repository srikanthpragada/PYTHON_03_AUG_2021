import os

allfiles = os.walk(r"c:\classroom\aug3\demo")
count = 0
for (dirname, dirs, files) in allfiles:
    for f in files:
        if f.endswith(".py"):
            print(dirname + "\\" + f)
            count += 1

print(f"Count = {count}")
