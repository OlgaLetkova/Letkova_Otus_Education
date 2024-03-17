from abc import ABC, abstractmethod


class Figure(ABC):
    """Figure class use for calculate area and perimeter different figures."""
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("You need use Figure")
        return self.get_area() + other_figure.get_area()