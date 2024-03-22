import pytest

from src.Square import Square


def test_area_square_positive(square_data):
    side_a, area, perimeter = square_data

    s = Square(side_a)
    assert s.get_area() == area, f"Area should be {side_a * side_a}"


def test_perimeter_square_positive(square_data):
    side_a, area, perimeter = square_data

    s = Square(side_a)
    assert s.get_perimeter() == perimeter, f"Perimeter should be {2 * (side_a + side_a)}"


def test_square_negative():
    with pytest.raises(ValueError):
        Square(-3)
        Square(0)
    with pytest.raises(AttributeError):
        Square("Test data")
        Square([1, 3, 6])
        Square({"first": 1, "second": 2})
        Square(True)
        Square({1, 2, 3})
