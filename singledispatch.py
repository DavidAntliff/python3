"""
Demonstration of functools.singledispatch.
https://docs.python.org/3/library/functools.html
"""
from functools import singledispatch


# dispatch on the type of the first argument
@singledispatch
def foo(x):
    desc = f"generic {x}"
    print(desc)
    return desc


@foo.register(int)
def _(x):
    desc = f"int {x}"
    print(desc)
    return desc


@foo.register(float)
def _(x):
    desc = f"float {x}"
    print(desc)
    return desc


class Generic(object):
    def __init__(self, x):
        self._x = x

    def __str__(self):
        return f"{self._x}"


assert foo(1) == "int 1"
assert foo(1.0) == "float 1.0"
assert foo(Generic(7)) == "generic 7"
