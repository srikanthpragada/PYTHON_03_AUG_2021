def isprime(n):
    pass


def iseven(n):
    return n % 2 == 0


def count_upper(st):
    count = 0
    for c in st:
        if c.isupper():
            count += 1

    return count


print(iseven(10))
print(iseven(13))

print(count_upper("Abc Xyz"))
