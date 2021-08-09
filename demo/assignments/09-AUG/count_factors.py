# Display count of factors for the given number

num = int(input("Enter number :"))

count = 0
for i in range(2, num // 2 + 1):
    if num % i == 0:
        count += 1

print(f"No. of factors : {count}")
