def extract_alpha(st):
    alphas = filter(str.isalpha, st)
    return "".join(alphas)


nums = [10, -3, 40, 0, 8, -44]

names = ['Java', 'Python', 'TypeScript', 'C#']
codes = ['ABC23X', "XYZ322Y", "BB3333Y"]

for n in sorted(map(abs, nums)):
    print(n)

data = "89,45,66,87"
marks = data.split(",")
print(marks)
print(sum(map(int, marks)))

for c in map(extract_alpha, codes):
    print(c)
