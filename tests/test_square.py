import pytest
from src.Square import Square


@pytest.mark.parametrize('side_a, perimetr, area',
                         [
                             (5, 20, 25),
                             (1 * 10 ** 31, 4 * 10 ** 31, 9 * 10 ** 62),
                             (0.1, 0.4, 0.01),
                             (1 / 6, 2 / 3, 1 / 36)
                         ])
def test_correct_Square(side_a, perimetr, area):
    r = Square(side_a)
    assert r.name == 'Square'
    assert r.get_area() == area
    assert r.get_perimetr() == perimetr


@pytest.mark.parametrize('side_a, perimetr, area',
                         [
                             (-3, -12, 9),
                             (0, 0, 0),
                             (-0.3, -1.2, 0.09),
                             (-1 / 6, -2 / 3, 1 / 36),
                             (10 ** 65, 4 * 10 ** 65, 10 ** 130),
                             ('5', '6', '22')
                         ])
def test_Square_creation_error(side_a, perimetr, area):
    with pytest.raises(ValueError):
        Square(side_a)


@pytest.mark.parametrize('side_a, area',
                         [
                             (1 * 10 ** 32, 4 * 10 ** 32, 1 * 10 ** 64)

                         ])
def test_get_square_area_error(side_a, perimetr, area):
    r = Square(side_a)
    with pytest.raises(ValueError):
        r.get_area() == area


@pytest.mark.parametrize('side_a, perimetr, area',
                         [
                             (35 * 10 ** 63, 4 * 10 ** 64, 1225 * 10 ** 126)
                         ])
def test_get_square_perimetr_error(side_a, perimetr, area):
    r = Square(side_a)
    with pytest.raises(ValueError):
        r.get_perimetr() == perimetr
