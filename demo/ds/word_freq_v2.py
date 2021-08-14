# Store Word freq

st = "This is Python and Python is a language any language is awesome if you understand it"
words = st.split()

word_freq = {}
for w in set(words):
    word_freq[w] = words.count(w)

for k, v in sorted(word_freq.items()):
    print(f"{k:10} {v:2}")
