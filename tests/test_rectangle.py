import pytest
from src.Rectangle import Rectangle


@pytest.mark.parametrize('side_a, side_b, perimetr, area',
                         [
                             (4, 5, 18, 20)
                         ])
def test_rectangle(side_a, side_b, perimetr, area):
    r = Rectangle(side_a, side_b)
    assert r.name == 'Rectangle'
    assert r.get_area() == area
    assert r.get_perimetr() == perimetr
