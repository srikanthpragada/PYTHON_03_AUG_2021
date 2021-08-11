# Take numbers until 0 and sort them

nums = []

while True:
    n = int(input("Enter number [0 to stop] :"))
    if n == 0:
        break

    nums.append(n)

nums.sort()

for n in nums:
    print(n)

