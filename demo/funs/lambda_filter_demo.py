nums = [10, -3, 40, 0, 8, -44]

for n in filter(lambda v: v >= 0, nums):
    print(n)

names = ['Java', 'Python', 'TypeScript', 'C#']

for s in filter(lambda s: len(s) > 4, names):
    print(s)
