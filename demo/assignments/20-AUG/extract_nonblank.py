def extract_non_blank(st):
    return st.replace(' ', '')


data = ["abc xyz", "pqr   def", "abcxyz", "kldjf lkjdlk  lkkjf"]

for s in map(extract_non_blank, data):
    print(s)
