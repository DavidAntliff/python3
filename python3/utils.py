def assert_raises(func, args, *, kwargs=None, exception_type=Exception, exception_str=None):
    try:
        func(*args, **kwargs if kwargs else {})
    except exception_type as e:
        print(e.__class__.__name__ + ": " + str(e))
        assert str(e) == exception_str, "Wrong exception message"
    except Exception as e:
        raise AssertionError(f"Wrong exception raised: expected {exception_type.__name__},"
                             f" caught {e.__class__.__name__}")
    else:
        raise AssertionError("No exception raised")


