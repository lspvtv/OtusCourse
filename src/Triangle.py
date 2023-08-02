import math
from math import sin


class Triangle:
    def __init__(self, side_a, side_b, side_c, angle_a, angle_b, angle_c):  # side a opposite angle a
        if angle_a + angle_b + angle_c != 180:
            raise ValueError("This triangle does not exist")
        if (angle_a >= 180 or angle_a <= 0) or (angle_b >= 180 or angle_b <= 0) or (angle_c >= 180 or angle_c <= 0):
            raise ValueError("This triangle does not exist")
        if type(angle_a) == str or type(angle_b) == str or type(angle_c) == str:
            raise ValueError("TypeError angle")
        if type(side_a) == str or type(side_b) == str or type(side_c) == str:
            raise ValueError("TypeError side")
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Can not create Triangle")
        if (side_a > 10 ** 64 or side_b > 10 ** 64 or side_c > 10 ** 64) or (
                angle_a > 10 ** 64 or angle_b > 10 ** 64 or angle_c > 10 ** 64):
            raise ValueError("It is too large, stack overflow")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.angle_a = angle_a
        self.angle_b = angle_b
        self.angle_c = angle_c
        self.name = 'Triangle'

    def get_area(self):
        area = round(0.5 * self.side_a * self.side_c * (sin(math.radians(self.angle_b)) * 180 / math.pi), 2)
        if area >= 10 ** 64:
            raise ValueError("It is too large, stack overflow")
        return area

    def get_perimetr(self):
        perimetr = round(self.side_a + self.side_b + self.side_c, 2)
        if perimetr >= 10 ** 64:
            raise ValueError("It is too large, stack overflow")
        return perimetr
