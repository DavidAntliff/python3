#!/usr/bin/env python

def f(a, b, *c, d=None):
    print(f"a {a}, b {b}, c {c}, d {d}")


def main():
    f(1, 2)          # a 1, b 2, c (), d None
    f(1, 2, 3)       # a 1, b 2, c (3,), d None
    f(1, 2, 3, 4)    # a 1, b 2, c (3, 4), d None
    f(1, 2, 3, d=4)  # a 1, b 2, c (3,), d 4


if __name__ == "__main__":
    main()
