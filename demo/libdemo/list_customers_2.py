def isvalidmobile(s):
    """
    Checks whether the given string is a valid mobile number.
    A valid mobile number is consisting of 10 digits

    :param s: String to test
    :return: True or False
    """
    return s.isdigit() and len(s) == 10


def isvalidname(s):
    """
    Checks whether the given name contains only Alphas and Spaces
    :param s: String to test
    :return: True or False
    """
    for c in s:
        if not (c.isalpha() or c == ' '):
            return False

    return True


f = open("customers2.txt", "rt")

customers = {}
for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) > 1:
        name = parts[0]
        mobile = parts[1]
        if not (isvalidname(name) and isvalidmobile(mobile)):
            continue

        if name in customers:
            customers[name].add(mobile)  # Add mobile to existing set of mobiles
        else:
            customers[name] = {mobile}  # Add a new entry with name and mobile

f.close()

for name, mobiles in sorted(customers.items()):
    print(f"{name:15} {','.join(sorted(mobiles))}")
