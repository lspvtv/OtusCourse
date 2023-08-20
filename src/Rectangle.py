from src.validation import validation
from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__()
        self.side_a = side_a
        self.side_b = side_b
        self.name = 'Rectangle'
        validation(self.side_a, self.side_b)

    def get_area(self):
        area = self.side_a * self.side_b
        validation(area)
        return area

    def get_perimetr(self):
        perimetr = 2 * (self.side_a + self.side_b)
        validation(perimetr)
        return perimetr
