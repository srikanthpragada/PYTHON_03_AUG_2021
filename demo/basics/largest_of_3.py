# Program to print largest of 3 numbers

n1 = int(input("Enter first number :"))
n2 = int(input("Enter second number :"))
n3 = int(input("Enter third number :"))

if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n3:
    print(n2)
else:
    print(n3)

