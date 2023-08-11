def validation(*args):
    for item in args:
        if type(item) == str:
            raise ValueError("TypeError")
        if item <= 0:
            raise ValueError("Can not create")
        if item > 10 ** 64:
            raise ValueError("It is too large, stack overflow")
