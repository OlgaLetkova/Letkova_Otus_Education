import pytest
from jsonschema import validate

from files import TXT_FILE_PATH
from schemas import schema_list_all, schema_one_dog, schema_list_all_sub_breeds
from urllib.parse import urlparse


def test_get_list_all_breeds(dog_api_client):
    response = dog_api_client.get_list_all_breeds()
    json_response = response.json()
    first_breed = json_response['message'].get('australian')
    assert response.status_code == 200
    assert json_response
    assert first_breed == ['shepherd']
    validate(instance=json_response, schema=schema_list_all)


@pytest.mark.parametrize(("status", "code", "image_format"),
                         [("success", 200, "jpg")])
def test_get_single_random_image(dog_api_client, status, code, image_format):
    response = dog_api_client.get_single_random_image()
    json_response = response.json()
    image_url = json_response['message']
    image_format_list = image_url.split('.')
    image_parse = urlparse(image_url)
    assert json_response
    assert image_format_list[3] == image_format
    assert image_parse.scheme == 'https'
    assert response.status_code == code
    assert json_response['status'] == status
    validate(instance=json_response, schema=schema_one_dog)


@pytest.mark.parametrize(("quantity", "status", "image_format"),
                         [("5", "success", "jpg")])
def test_get_multiple_random_images(dog_api_client, quantity, status, image_format):
    response = dog_api_client.get_multiple_random_images(quantity)
    json_response = response.json()
    image_url_list = json_response['message']
    assert json_response
    assert response.ok
    assert json_response['status'] == status
    assert len(image_url_list) == int(quantity)
    i = 0
    for i in range(0, 5):
        assert image_format in image_url_list[i].split('.')[3]


def test_get_single_random_sub_breed_image(dog_api_client, dog_data):
    sub_breed, status, code, image_format = dog_data
    response = dog_api_client.get_single_random_sub_breed_image(sub_breed)
    json_response = response.json()
    image_url = json_response['message']
    image_format_list = image_url.split('.')
    image_parse = urlparse(image_url)
    assert json_response
    assert image_format_list[3] == image_format
    assert image_parse.scheme == 'https'
    assert response.status_code == code
    assert json_response['status'] == status
    validate(instance=json_response, schema=schema_one_dog)
    url_list = image_url.split('/')
    assert url_list[4] == f"hound-{sub_breed}"


def test_get_list_all_sub_breeds(dog_api_client):
    response = dog_api_client.get_list_all_sub_breeds()
    json_response = response.json()
    sub_breeds_list = json_response['message']
    assert response.status_code == 200
    assert json_response
    validate(instance=json_response, schema=schema_list_all_sub_breeds)
    with open(TXT_FILE_PATH, "r") as file:
        etalon_list = file.readline().split(",")
        assert sub_breeds_list == etalon_list
