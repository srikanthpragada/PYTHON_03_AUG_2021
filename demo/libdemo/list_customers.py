f = open("customers.txt", "rt")

customers = []
for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) > 1:
       customers.append((parts[0], parts[1]))

f.close()

for name, mobile in sorted(customers):
    print(f"{name:15} {mobile}")
