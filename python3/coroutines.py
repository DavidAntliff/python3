"""Based on http://dabeaz.com/coroutines/Coroutines.pdf"""


def coroutine(func):
    """Decorator to prime a coroutine by calling next()."""
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start


@coroutine
def grep(pattern):
    print(f"Looking for {pattern}")
    try:
        while True:
            line = (yield)
            if pattern in line:
                print(line)
    except GeneratorExit:
        print("Going away. Goodbye.")


g = grep("hello")
g.send("hi")
g.send("hello!")
g.close()


def source(target):
    for item in [1, 2, 3, 4, 5]:
        target.send(item)
    target.close()


@coroutine
def sink(name):
    try:
        while True:
            item = (yield)
            print(name + " " + str(item))
    except GeneratorExit:
        print(name + " sink closed")


source(sink("sink"))


@coroutine
def filter(target, mult=2):
    while True:
        item = (yield)
        item *= mult
        target.send(item)

source(filter(sink("sink")))


@coroutine
def broadcast(targets):
    while True:
        item = (yield)
        for target in targets:
            target.send(item)

source(
    broadcast(
        (filter(sink("A"), 1),
         filter(sink("B"), 2),
         filter(sink("C"), 3)
         )
    )
)

sink_D = sink("D")
source(
    broadcast(
        (filter(sink_D, 1),
         filter(sink_D, 2))
    )
)


@coroutine
def wrapper(target):
    yield from target


source(filter(wrapper(sink("sink"))))
