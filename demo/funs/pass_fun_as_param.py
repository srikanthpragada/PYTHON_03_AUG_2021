def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def process(a, b, func):
    print(func(a, b))


process(10, 20, multiply)
process(100, 200, add)
process(10, 20, print)
