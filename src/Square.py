from src.Rectangle import Rectangle


class Square(Rectangle):
    """Square use only one side_a for calculate area and perimeter."""

    def __init__(self, side_a: int | float):
        super().__init__(side_a, side_a)
        self.name = "Square"
        self.side_a = side_a
