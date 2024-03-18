from src.Rectangle import Rectangle


class Square(Rectangle):
    """Square use only one side_a for calculate area and perimeter."""
    def __init__(self, side_a: int):
        if side_a <= 0:
            raise ValueError("side_a should be greate than 0")
        super().__init__(side_a, side_a)
        self.name="Square"


