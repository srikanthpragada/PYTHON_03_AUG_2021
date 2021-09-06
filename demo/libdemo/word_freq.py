def getword(s):
    return s.strip(' .:?,;"')


with open(r"c:\classroom\old_man.txt", "rt") as f:
    content = f.read()
    content = content.replace("\n", ' ').replace("'", " ")

words = content.split(' ')
# Remove new line and other non-word chars from words
words = list(map(getword, words))
word_freq = {}

for w in set(words):
    if len(w) > 0:
        word_freq[w] = words.count(w)

for word, count in sorted(word_freq.items()):
    print(f"{word:15}  {count:3}")
