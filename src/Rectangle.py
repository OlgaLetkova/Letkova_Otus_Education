from src.Figure import Figure


class Rectangle(Figure):
    """Rectangle class use two sides: side_a and side_b for calculate area and perimeter."""

    def __init__(self, side_a: int | float, side_b: int | float):
        super().__init__(name="Rectangle")
        if type(side_a) not in [int, float] or type(side_b) not in [int, float]:
            raise AttributeError("side_a and side_b should have type int or float")
        if side_a <= 0 or side_b <= 0:
            raise ValueError("side_a and side_b should be greate than 0")
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)
