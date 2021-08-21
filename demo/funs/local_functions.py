g = 1

def first():
    global g
    a = 100     # Enclosing
    g = 2
    print("In First")

    # Local Function / Nested function
    def second():
        nonlocal a
        print("In Second")
        b = 1000    # Local variable
        a = 200     # Refer to enclosing variable
        print(g, a, b)

    second()  # Call local function
    print(a)

first()