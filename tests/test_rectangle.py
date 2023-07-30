import pytest
from src.Rectangle import Rectangle


@pytest.mark.parametrize('side_a, side_b, perimetr, area',
                         [
                             (-4, 5, 2, -20),
                             (0, 20, 40, 0),
                             (0, 0, 0, 0),
                             (-2, -3, -10, -6),
                             (4, 4, 16, 16),
                             (10 ** 65, 10 ** 27, 11 * 10 ** 26, 10 ** 52),
                             (10 ** 15, 10 ** 65, 11 * 10 ** 26, 10 ** 52),
                             ('5', '6', '22', '30')
                         ])
def test_rectangle_creation_error(side_a, side_b, perimetr, area):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


@pytest.mark.parametrize('side_a, side_b, perimetr, area',
                         [
                             (1 * 10 ** 32, 9 * 10 ** 32, 10 ** 33, 9 * 10 ** 64)
                         ])
def test_get_area_error(side_a, side_b, perimetr, area):
    r = Rectangle(side_a, side_b)
    with pytest.raises(ValueError):
        r.get_area() == area


@pytest.mark.parametrize('side_a, side_b, perimetr, area',
                         [
                             (1 * 10 ** 63, 9 * 10 ** 63, 10 ** 64, 9 * 10 ** 126)
                         ])
def test_get_perimetr_error(side_a, side_b, perimetr, area):
    r = Rectangle(side_a, side_b)
    with pytest.raises(ValueError):
        r.get_perimetr() == perimetr
