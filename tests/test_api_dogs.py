import pytest
from jsonschema import validate

from schemas import schema_list_all, schema_one_dog
from urllib.parse import urlparse


def test_get_list_all_breeds(api_client):
    response = api_client.get_list_all_breeds()
    json_response = response.json()
    first_breed = json_response['message'].get('australian')
    assert response.status_code == 200
    assert json_response
    assert first_breed == ['shepherd']
    validate(instance=json_response, schema=schema_list_all)


@pytest.mark.parametrize(("status", "code", "image_format"),
                         [("success", 200, "jpg")])
def test_get_random_image(api_client, status, code, image_format):
    response = api_client.get_random_image()
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
