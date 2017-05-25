#!/usr/bin/env python
"""Requires Python 3.6 or newer."""


def assert_raises(func, args, *, kwargs=None, exception_type=Exception, exception_str=None):
    try:
        func(*args, **kwargs if kwargs else {})
    except exception_type as e:
        print(e.__class__.__name__ + ": " + str(e))
        assert str(e) == exception_str
    except Exception as e:
        raise AssertionError(f"Wrong exception raised: expected {exception_type.__name__},"
                             f" caught {e.__class__.__name__}")
    else:
        raise AssertionError("No exception raised")


def f(a, b, *c, d=None):
    r = f"a {a}, b {b}, c {c}, d {d}"
    print(r)
    return r


def g(a, b, *, c, d=None):
    """c is mandatory!"""
    r = f"a {a}, b {b}, c {c}, d {d}"
    print(r)
    return r


assert f(1, 2) == "a 1, b 2, c (), d None"
assert f(1, 2, 3) == "a 1, b 2, c (3,), d None"
assert f(1, 2, 3, 4) == "a 1, b 2, c (3, 4), d None"
assert f(1, 2, 3, d=4) == "a 1, b 2, c (3,), d 4"

assert_raises(g, (1, 2), exception_type=TypeError,
              exception_str="g() missing 1 required keyword-only argument: 'c'")
assert_raises(g, (1, 2, 3), exception_type=TypeError,
              exception_str="g() takes 2 positional arguments but 3 were given")
assert_raises(g, (1, 2), kwargs={'d': 3}, exception_type=TypeError,
              exception_str="g() missing 1 required keyword-only argument: 'c'")

assert g(1, 2, c=3) == "a 1, b 2, c 3, d None"
assert g(1, 2, c=3, d=4) == "a 1, b 2, c 3, d 4"
