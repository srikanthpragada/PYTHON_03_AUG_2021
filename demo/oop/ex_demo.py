data = input("Enter number :")

try:
    num = int(data)
    result = 100 / num
    print(f"Result = {result}")
except ValueError as ex:
    print("Sorry! Invalid number!")
except ZeroDivisionError:
    print("Sorry! Please enter value higher than zero!")
except Exception as ex:
    print("Sorry! Error --> ", ex)
else:
    print("Success")
finally:
    print("Over")

print("The End")
