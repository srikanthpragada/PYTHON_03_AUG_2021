# Count upper, lower and digits

st = input("Enter a string :")
upper = lower = digit = 0

for c in st:
    if c.isupper():
        upper += 1
    elif c.islower():
        lower += 1
    elif c.isdigit():
        digit += 1


print(f"Upper = {upper}, Lower = {lower}, Digits = {digit}")
