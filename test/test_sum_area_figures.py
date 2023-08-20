import pytest
from src.Figure import Figure
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
from src.Circle import Circle


def test_sum_area_rectangle_square():
    value1 = Rectangle(2, 3)
    value2 = Square(5)
    assert value1.sum_area(value2) == 31


def test_sum_area_rectangle_triangle():
    value1 = Rectangle(2, 3)
    value2 = Triangle(5, 3, 2, 100, 20, 60)
    assert value1.sum_area(value2) == 103.98


def test_sum_area_rectangle_circle():
    value1 = Rectangle(2, 3)
    value2 = Circle(5, 3, 5)
    assert value1.sum_area(value2) == 84.54


def test_sum_area_square_triangle():
    value1 = Square(2)
    value2 = Triangle(5, 3, 2, 100, 20, 60)
    assert value1.sum_area(value2) == 101.98


def test_sum_area_square_circle():
    value1 = Square(2)
    value2 = Circle(5, 3, 2)
    assert value1.sum_area(value2) == 16.57


def test_sum_area_triangle_circle():
    value1 = Triangle(5, 3, 2, 100, 20, 60)
    value2 = Circle(5, 3, 2)
    assert round(value1.sum_area(value2), 2) == 110.55
