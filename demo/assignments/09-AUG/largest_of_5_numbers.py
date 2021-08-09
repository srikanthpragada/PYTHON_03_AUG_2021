# Print largest of 5 numbers

largest = 0
for i in range(5):
    n = int(input("Enter a number :"))
    if n > largest:
        largest = n

print(f"Largest = {largest}")
