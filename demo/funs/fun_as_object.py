# Function as object

def fun():
    print("fun()")


print(id(fun))


def fun(msg):
    print(msg)


print(id(fun))

# fun()
fun("Hello")
