import math


class Circle:
    def __init__(self, coord_x, coord_y, radius):
        if type(coord_x) == str or type(coord_y) == str or type(radius) == str:
            raise ValueError("TypeError")
        if radius <= 0:
            raise ValueError("Can not create Circle")
        if coord_x > 10 ** 64 or coord_y > 10 ** 64 or radius > 10 ** 64:
            raise ValueError("It is too large, stack overflow")
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.radius = radius
        self.name = 'Circle'

    def get_area(self):
        area = math.pi * self.radius ** 2
        if area >= 10 ** 64:
            raise ValueError("It is too large, stack overflow")
        return area

    def get_length(self):
        length = round(2 * math.pi * self.radius, 2)
        if length >= 10 ** 64:
            raise ValueError("It is too large, stack overflow")
        return length
