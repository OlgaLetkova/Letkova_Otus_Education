from src.Figure import Figure


class Circle(Figure):
    """Circle class use radius for calculate area"""

    def __init__(self, radius: int):
        super().__init__(name="Circle")
        if type(radius) != int:
            raise AttributeError("radius should have type int")
        if radius <= 0:
            raise ValueError("radius should be greate than 0")
        self.radius = radius

    def get_area(self) -> any:
        PI = 3.14
        return PI * (self.radius ** 2)

    def get_perimeter(self):
        pass

