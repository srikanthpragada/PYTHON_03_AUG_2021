# Positional-only arguments
def wish(name="Guest", message='Hi', /):
    pass


wish("Abc", "Hello")
wish("Andy")
# wish(message="Hello", name="Anders")
