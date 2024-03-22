import pytest


@pytest.fixture(params=[(4, 6, 8, 11.619, 18), (9.5, 8.4, 4.5, 18.899, 22.4)], ids=["int", "float"])
def triangle_data(request):
    side_a, side_b, side_c, area, perimeter = request.param
    yield side_a, side_b, side_c, area, perimeter


@pytest.fixture(params=[(6, 36, 24), (12.5, 156.25, 50)], ids=["int", "float"])
def square_data(request):
    side_a, area, perimeter = request.param
    yield side_a, area, perimeter


@pytest.fixture()
def circle_data():
    def _wrapper(data: str):
        if data == "integer":
            return 12, 452.16
        if data == "float":
            return 4.5, 63.585
    yield _wrapper

    print("\n Down")
