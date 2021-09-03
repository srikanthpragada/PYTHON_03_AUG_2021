total = 0
count = 0
while True:
    try:
        v = int(input("Enter number :"))
        total += v
        count += 1
        if count == 5:
            break
    except:
        print("Invalid number!")

print(f"Total = {total}")
