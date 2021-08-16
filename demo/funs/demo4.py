def wish(name, message="Hi"):
    print(message, name)


wish("Van")  # Positional
wish("Steve", "Hello")
wish(message="Good Morning", name="Scott")  # Keyword
wish(name="Andy")
