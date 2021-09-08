def numbers():
    for i in range(5):
        yield i


evens = (n for n in range(2, 11, 2))
evens2 = [n for n in range(2, 11, 2)]

print(type(evens))

nums = numbers()
print(type(nums))

print(next(nums))
print(next(nums))
