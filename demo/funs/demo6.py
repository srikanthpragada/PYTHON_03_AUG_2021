def wish(*names, message='Hi'):
    print(type(names))
    for n in names:
        print(message, n)


def greet(message='Hi', *names):
    pass


greet('Bill', 'Andy')

wish(10, "Jack", "Bill", message="Hello")
wish("Larry", "Garry", "Karry")
