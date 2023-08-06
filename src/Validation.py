class Validation:
    def __init__(self, **kwargs):
        if type(kwargs) == str:
            raise ValueError("TypeError")
        if kwargs <= 0:
            raise ValueError("Can not create")
        if kwargs > 10 ** 64:
            raise ValueError("It is too large, stack overflow")
