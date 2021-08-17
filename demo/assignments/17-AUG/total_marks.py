
st = "87,45,77,56,93"

marks = st.split(",")
total = 0
for m in marks:
    total += int(m)

print(total)
