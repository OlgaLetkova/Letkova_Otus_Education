import pytest
from jsonschema import validate

from file_helpers.csv_helper import read_lines_from_csv
from schemas import schema_one_resource
from pydantic import BaseModel


class ResourceBaseModel(BaseModel):
    title: str
    body: str
    userId: int


def test_get_all_resources(placeholder_api_client):
    response = placeholder_api_client.get_all_resources()
    json_response = response.json()
    assert json_response
    assert response.ok
    for resource in json_response:
        validate(instance=resource, schema=schema_one_resource)
    assert len(json_response) == 100


def test_create_one_resource(placeholder_api_client):
    data = ResourceBaseModel(title="Khokhloma painting",
                             body="Typical color schemes for Khokhloma include a combination of red, black, and gold.",
                             userId=6)
    headers = {"Content-type": "application/json; charset=UTF-8"}

    response = placeholder_api_client.create_one_resource(data=dict(data))
    json_response = response.json()
    assert response.ok
    validate(instance=json_response, schema=schema_one_resource)
    assert json_response["id"] == 101
    assert response.headers["Content-type"] == headers["Content-type"].lower()


@pytest.mark.parametrize("data", read_lines_from_csv())
def test_update_one_resource(placeholder_api_client, data):
    headers = {"Content-type": "application/json; charset=UTF-8"}
    response = placeholder_api_client.update_one_resource(data=data, resource_number=data["id"])
    json_response = response.json()
    assert response.status_code == 200
    assert json_response["title"] == data["title"]
    assert json_response["body"] == data["body"]
    assert response.headers["Content-type"] == headers["Content-type"].lower()


@pytest.mark.parametrize(("_id", "code", "title"),
                         [(6, 200, "VDNKh is located in Ostankinsky District of Moscow near Ostankino Tower.")])
def test_patch_one_resource_by_id(placeholder_api_client, _id, code, title):
    data = {
        "title": title
    }
    response = placeholder_api_client.patch_one_resource(data=data, resource_number=_id)
    json_response = response.json()
    assert json_response
    assert json_response['id'] == _id
    assert response.status_code == code
    assert json_response['title'] == title


@pytest.mark.parametrize('_id', [-6, 0, 'value'])
def test_get_one_resource_by_id_invalid_data(placeholder_api_client, _id):
    response = placeholder_api_client.get_one_resource_by_id(resource_number=_id)
    assert response.status_code != 200
    assert response.json() == {}
