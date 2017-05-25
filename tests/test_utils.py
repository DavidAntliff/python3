import pytest

import python3.utils as utils


def test_assert_raises_passes_with_correct_exception():
    def f():
        raise TypeError("A type error.")
    utils.assert_raises(f, (), exception_type=TypeError, exception_str="A type error.")


def test_assert_raises_with_no_exception():
    def f():
        ...

    with pytest.raises(AssertionError, message="No exception raised"):
        utils.assert_raises(f, (), exception_type=None, exception_str=None)


def test_assert_raises_for_wrong_exception_message():
    def raise_exception(exception_type, exception_message):
        raise exception_type(exception_message)

    with pytest.raises(AssertionError, message="Wrong exception message"):
        utils.assert_raises(raise_exception, (TypeError, "12345"),
                            exception_type=TypeError,
                            exception_str="123456")


def test_assert_raises_with_keyword_arguments():
    def f(a, b):
        if a == b:
            raise ValueError("values are equal.")

    utils.assert_raises(f, (3,), kwargs={'b': 3},
                        exception_type=ValueError,
                        exception_str="values are equal.")

    utils.assert_raises(f, (), kwargs={'a': 3, 'b': 3},
                        exception_type=ValueError,
                        exception_str="values are equal.")
