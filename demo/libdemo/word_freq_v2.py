import re

with open(r"c:\classroom\old_man.txt", "rt") as f:
    content = f.read()

words = re.findall(r"\w+", content)
word_freq = {}

for w in set(words):
    word_freq[w] = words.count(w)

for word, count in sorted(word_freq.items()):
    print(f"{word:15}  {count:3}")
