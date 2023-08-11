import math
from src.validation import validation


class Circle:
    def __init__(self, coord_x, coord_y, radius):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.radius = radius
        self.name = 'Circle'
        validation(self.coord_x, self.coord_y, self.radius)

    def get_area(self):
        area = math.pi * self.radius ** 2
        validation(area)
        return area

    def get_length(self):
        length = round(2 * math.pi * self.radius, 2)
        validation(length)
        return length
