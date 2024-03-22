import pytest

from src.Rectangle import Rectangle


@pytest.mark.parametrize(("side_a", "side_b", "area"),
                         [
                             (3, 5, 15),
                             (3.5, 5.5, 19.25)
                         ],
                         ids=["integer", "float"])
def test_area_rectangle_positive(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.get_area() == area, f"Area should be {side_a * side_b}"


@pytest.mark.parametrize(("side_a", "side_b", "perimeter"),
                         [
                             (2, 4, 12),
                             (0.5, 4.5, 10)
                         ],
                         ids=["integer", "float"])
def test_perimeter_rectangle_positive(side_a, side_b, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.get_perimeter() == perimeter, f"Perimeter should be {2 * (side_a + side_b)}"


def test_rectangle_negative():
    with pytest.raises(ValueError):
        Rectangle(-3, 5)
        Rectangle(4, -7)
        Rectangle(3, 0)
        Rectangle(0, 6)
        Rectangle(0, 0)
        Rectangle(-6, -6)
    with pytest.raises(AttributeError):
        Rectangle("Test data", 6)
        Rectangle(3.7, [1, 3, 6])
        Rectangle({"first": 1, "second": 2}, 5)
        Rectangle(True, 6)
        Rectangle(1, {1, 2, 3})
        Rectangle(2, False)
