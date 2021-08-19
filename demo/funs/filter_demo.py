def ispositive(n):
    return n >= 0


def isbigname(name):
    return len(name) > 4


nums = [10, -3, 40, 0, 8, -44]

for n in filter(ispositive, nums):
    print(n)

for c in filter(str.isupper, "AbcXyz"):
    print(c)

names = ['Java', 'Python', 'TypeScript', 'C#']

for s in filter(isbigname, names):
    print(s)
