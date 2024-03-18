import math

from src.Figure import Figure


class Triangle(Figure):
    """Triangle class use three sides: side_a, side_b, side_c for calculate area and perimeter"""

    def __init__(self, side_a: int, side_b: int, side_c: int):
        super().__init__(name="Triangle")
        if type(side_a) != int or type(side_b) != int or type(side_c) != int:
            raise AttributeError("side_a, side_b, side_c should have type int")
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("side_a, side_b, side_c should be greate than 0")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self) -> any:
        p = self.get_perimeter() / 2
        return math.sqrt((p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)))

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

