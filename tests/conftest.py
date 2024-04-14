import pytest
import requests

from src.api_clients.brewery_api_client import BreweryApiClient
from src.api_clients.dog_api_client import DogsApiClient
from src.api_clients.placeholder_api_client import PlaceholderApiClient


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


@pytest.fixture(scope="session")
def dog_api_client():
    client = DogsApiClient()
    return client


@pytest.fixture(params=[("afghan", "success", 200, "jpg"),
                        ("blood", "success", 200, "jpg"),
                        ("walker", "success", 200, "jpg")])
def dog_data(request):
    sub_breed, status, code, image_format = request.param
    yield sub_breed, status, code, image_format


@pytest.fixture(scope="session")
def brewery_api_client():
    client = BreweryApiClient()
    return client


@pytest.fixture(params=[("06e9fffb-e820-45c9-b107-b52b51013e8f", "12Degree Brewing", 200, "http://www.12degree.com"),
                        ("701239cb-5319-4d2e-92c1-129ab0b3b440", "Bière de la Plaine", 200,
                         "https://brasseriedelaplaine.fr/")])
def brewery_data(request):
    _id, name, code, website_url = request.param
    yield _id, name, code, website_url


@pytest.fixture(scope="session")
def placeholder_api_client():
    client = PlaceholderApiClient()
    return client


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru/",
        help="This is request url"
    )

    parser.addoption(
        "--status_code",
        default=200,
        help="Status code for request url"
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")
