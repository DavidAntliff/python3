import os


def f(x):
    try:
        os.stat("foo")
    except OSError:
        raise NotImplementedError("TODO")


try:
    f(1)
except Exception as e:
    # must assign e to a variable to be visible to pdb!
    exc = e
    # import pdb; pdb.set_trace()
    print(exc)
    print("Original Cause: " + str(exc.__cause__))
    print("Original Traceback: " + str(exc.__traceback__))
    print("Original Context: " + str(exc.__context__))
    context = exc.__context__
    print("Context cause: " + str(context.__cause__))
    print("Context traceback: " + str(context.__traceback__))
    print("Context's context: " + str(context.__context__))
