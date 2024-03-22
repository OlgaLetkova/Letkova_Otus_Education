import pytest

from src.Circle import Circle


@pytest.mark.parametrize("circle_type_date", ["integer", "float"])
def test_area_circle_positive(circle_data, circle_type_date):
    radius, area = circle_data(data=circle_type_date)

    c = Circle(radius)
    assert c.get_area() == area, f"Area should be {3.14 * (radius ** 2)}"


def test_circle_negative():
    with pytest.raises(ValueError):
        Circle(-3)
        Circle(0)
    with pytest.raises(AttributeError):
        Circle("Test data")
        Circle([1, 3, 6])
        Circle({"first": 1, "second": 2})
        Circle(True)
        Circle({1, 2, 3})
