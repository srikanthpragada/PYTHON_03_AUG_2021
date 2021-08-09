# Accept numbers until 0 is given and display total

total = 0

while True:
    n = int(input("Enter a number [0 to stop] :"))
    if n == 0:
        break    # Stop loop

    if n < 0:
        continue

    # Process
    total += n

print(f'Total = {total}')
