# Keyword args
def process(**kwargs):
    print(kwargs)


def task(*args, **kwargs):
    pass


process(a=10, b=20, c='abc')
task(10, 20, x=10, y=20)
