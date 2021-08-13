# Word freq

st = "This is Python and Python is a language"
words = st.split()

for w in sorted(set(words)):
    print(f"{w:10}  {words.count(w):2}")
