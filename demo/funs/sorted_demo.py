nums = [10, -3, 40, 0, 8, -44]
names = ['Java', 'python', 'typeScript', 'C#', 'JavaScript', 'c']

for n in sorted(nums, key=abs):
    print(n)

for n in sorted(names, key=str.upper):
    print(n)
