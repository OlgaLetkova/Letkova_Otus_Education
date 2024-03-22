import pytest

from src.Triangle import Triangle


def test_perimeter_triangle_positive(triangle_data):
    side_a, side_b, side_c, area, perimeter = triangle_data
    t = Triangle(side_a, side_b, side_c)
    assert t.get_perimeter() == perimeter, f"Perimeter should be {side_a + side_b + side_c}"


def test_area_triangle_positive(triangle_data):
    side_a, side_b, side_c, area, perimeter = triangle_data
    t = Triangle(side_a, side_b, side_c)
    assert t.get_area() == area


def test_triangle_negative():
    with pytest.raises(ValueError):
        Triangle(-3, 5, 9)
        Triangle(4, -7, 3)
        Triangle(4, 7, -3)
        Triangle(3, 0, 6)
        Triangle(0, 6, 9)
        Triangle(2, 6, 0)
        Triangle(0, 0, 0)
        Triangle(-6, -12, -3)
    with pytest.raises(AttributeError):
        Triangle("Test data", 6, 11)
        Triangle(12, "Test data", 11)
        Triangle(11, 3, "Test data")
        Triangle(3.7, [1, 3, 6], 14)
        Triangle({"first": 1, "second": 2}, 5, 8)
        Triangle(True, 6, 8)
        Triangle(1, 12, {1, 2, 3})
        Triangle(2, False, 11)
        Triangle(5, 11, True)
