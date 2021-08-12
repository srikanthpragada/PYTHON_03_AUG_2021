# Validating PAN

pan = "ABCDE7654E"

if pan[:5].isalpha() and pan[5:9].isdigit() and pan[-1].isalpha():
    print("Valid PAN")
else:
    print("Invalid PAN")