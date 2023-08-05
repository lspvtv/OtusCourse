import pytest
from src.Circle import Circle


@pytest.mark.parametrize('coord_x, coord_y, radius, area, length',
                         [
                             (1, 2, 5, 78.54, 31.42),
                             (-1, 2, 5, 78.54, 31.42),
                             (1, -2, 5, 78.54, 31.42),
                             (-1, -2, 5, 78.54, 31.42),
                             (0, 0, 5, 78.54, 31.42)
                         ])
def test_correct_circle(coord_x, coord_y, radius, area, length):
    r = Circle(coord_x, coord_y, radius)
    assert r.name == 'Circle'
    assert round(r.get_area(), 2) == area
    assert round(r.get_length(), 2) == length


@pytest.mark.parametrize('coord_x, coord_y, radius',
                         [
                             (0, 0, 0),
                             (0, 0, -5),
                             ('2', '3', 10),
                             (0, 0, '10'),
                             (0, 0, 10 ** 65)
                         ])
def test_circle_creation_error(coord_x, coord_y, radius):
    with pytest.raises(ValueError):
        Circle(coord_x, coord_y, radius)


@pytest.mark.parametrize('coord_x, coord_y, radius, area, length',
                         [
                             (0, 0, 50 * 10 ** 33, 25 * 10 ** 67, 31 * 10 ** 63)

                         ])
def test_get_circle_area_error(coord_x, coord_y, radius, area, length):
    r = Circle(coord_x, coord_y, radius)
    with pytest.raises(ValueError):
        round(r.get_area(), 2) == area


@pytest.mark.parametrize('coord_x, coord_y, radius, area, length',
                         [
                             (0, 0, 50 * 10 ** 62, 25 * 10 ** 126, 31 * 10 ** 64)
                         ])
def test_get_circle_length_error(coord_x, coord_y, radius, area, length):
    r = Circle(coord_x, coord_y, radius)
    with pytest.raises(ValueError):
        round(r.get_length(), 2) == length
