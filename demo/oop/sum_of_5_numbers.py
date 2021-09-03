total = 0

for n in range(5):
    try:
        v = int(input("Enter number :"))
        total += v
    except:
        print("Invalid number!")

print(f"Total = {total}")
