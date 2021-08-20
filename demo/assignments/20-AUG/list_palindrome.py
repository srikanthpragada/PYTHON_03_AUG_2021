def ispalindrome(n):
    s = str(abs(n))
    return s == s[::-1]


nums = [121, 156, 888, 2332, 897, -11]

for n in filter(ispalindrome, nums):
    print(n)
