import pytest
from src.Triangle import Triangle


@pytest.mark.parametrize('side_a, side_b, side_c, angle_a, angle_b, angle_c, area, perimetr',
                         [
                             (10, 10, 10, 60, 60, 60, 2480.98, 30),
                             (7, 7, 5, 69.075, 69.075, 41.85, 936.55, 19),
                             (5, 7, 3, 38.21, 120, 21.79, 372.15, 15),
                             (8, 8.94, 4, 63.435, 90, 26.565, 916.73, 20.94),
                             (9, 2, 10, 54.9, 10.48, 114.62, 468.97, 21)
                         ])
def test_correct_triangle(side_a, side_b, side_c, angle_a, angle_b, angle_c, area, perimetr):
    r = Triangle(side_a, side_b, side_c, angle_a, angle_b, angle_c)
    assert r.name == 'Triangle'
    assert r.get_area() == area
    assert r.get_perimetr() == perimetr


@pytest.mark.parametrize('side_a, side_b, side_c, angle_a, angle_b, angle_c, area, perimetr',
                         [
                             (-4, -5, -7, 40, 50, 90, 13, 15),
                             (4, 5, 7, -40, -50, -90, 13, 15),
                             (0, 20, 0, 40, 30, 110, 0, 0),
                             (13, 20, 23, 80, 0, 110, 0, 0),
                             (0, 0, 0, 0, 0, 0, 0, 0),
                             (10 ** 65, 10 ** 65, 10 ** 65, 110, 40, 30, 40, 50),
                             ('10', '10', '10', 60, 60, 60, '2480.98', '30'),
                             (10, 10, 10, '60', '60', '60', '2480.98', '30')
                         ])
def test_triangle_creation_error(side_a, side_b, side_c, angle_a, angle_b, angle_c, area, perimetr):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c, angle_a, angle_b, angle_c)


@pytest.mark.parametrize('side_a, side_b, side_c, angle_a, angle_b, angle_c, area, perimetr',
                         [
                             (1 * 10 ** 33, 9 * 10 ** 35, 10 ** 31, 10, 80, 90, 8 * 10 ** 72, 9 * 10 ** 63)
                         ])
def test_get_triangle_area_error(side_a, side_b, side_c, angle_a, angle_b, angle_c, area, perimetr):
    r = Triangle(side_a, side_b, side_c, angle_a, angle_b, angle_c)

    with pytest.raises(ValueError):
        r.get_area() == area


@pytest.mark.parametrize('side_a, side_b, side_c, angle_a, angle_b, angle_c, area, perimetr',
                         [
                             (1 * 10 ** 63, 9 * 10 ** 63, 10 ** 63, 10, 80, 90, 8 * 10 ** 62, 9 * 10 ** 125)
                         ])
def test_get_triangle_perimetr_error(side_a, side_b, side_c, angle_a, angle_b, angle_c, area, perimetr):
    r = Triangle(side_a, side_b, side_c, angle_a, angle_b, angle_c)
    with pytest.raises(ValueError):
        r.get_perimetr() == perimetr
