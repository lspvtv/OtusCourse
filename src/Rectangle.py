class Rectangle:
    def __init__(self, side_a, side_b):
        if type(side_a) == str or type(side_b) == str:
            raise ValueError("TypeError")
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Can not create Rectangle")
        if side_a > 10 ** 64 or side_b > 10 ** 64:
            raise ValueError("It is too large, stack overflow")
        self.side_a = side_a
        self.side_b = side_b
        self.name = 'Rectangle'

    def get_area(self):
        area = self.side_a * self.side_b
        if area >= 10 ** 64:
            raise ValueError("It is too large, stack overflow")
        return area

    def get_perimetr(self):
        perimetr = 2 * (self.side_a + self.side_b)
        if perimetr >= 10 ** 64:
            raise ValueError("It is too large, stack overflow")
        return perimetr
