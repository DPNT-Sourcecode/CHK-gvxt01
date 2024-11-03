# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    assert isinstance(x, int) and isinstance(y, int), "inputs must be of type integer"
    assert x >= 0 and x <= 100, "x must be between 0 and 100"
    assert y >= 0 and y <= 100, "y must be between 0 and 100"

    return x + y


