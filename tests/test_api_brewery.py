import pytest
from jsonschema import validate

from schemas import schema_one_brewery


@pytest.mark.parametrize(("_id", "code", "name"),
                         [("b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0", 200, "MadTree Brewing 2.0")])
def test_get_single_brewery_by_id(brewery_api_client, _id, code, name):
    response = brewery_api_client.get_single_brewery_by_id(_id)
    json_response = response.json()
    assert json_response
    assert json_response['id'] == _id
    assert response.status_code == code
    assert json_response['name'] == name
    validate(instance=json_response, schema=schema_one_brewery)


def test_get_brewery_by_city(brewery_api_client):
    query = {"by_city": "san_diego",
             "per_page": "3"}
    response = brewery_api_client.get_brewery_by_city(query)
    json_response = response.json()
    assert response.status_code == 200
    assert len(json_response) == int(query["per_page"])
    for brewery in json_response:
        assert brewery["city"] == "San Diego"
        assert brewery["id"] is not None


@pytest.mark.parametrize(["state", "code"],
                         [("California", 200), ("Texas", 200), ("Oklahoma", 200)])
def test_get_brewery_by_state(brewery_api_client, state, code):
    query = {"by_state": state,
             "per_page": "3"}
    response = brewery_api_client.get_brewery_by_state(query)
    json_response = response.json()
    assert json_response
    assert response.status_code == code
    assert len(json_response) == int(query["per_page"])
    for brewery in json_response:
        assert brewery["state"] == state


def test_get_brewery_by_ids(brewery_api_client, brewery_data):
    _id, name, code, website_url = brewery_data
    query = {"by_ids": brewery_data[0]}
    response = brewery_api_client.get_brewery_by_ids(query)
    json_response = response.json()
    assert json_response
    assert response.status_code == code
    for brewery in json_response:
        assert brewery["name"] == name
        assert brewery["id"] == _id
        assert brewery["website_url"] == website_url


@pytest.mark.parametrize(["size", "code"],
                         [(4, 200), (50, 200)])
def test_get_number_of_breweries_by_size(brewery_api_client, size, code):
    query = {"size": size}
    response = brewery_api_client.get_number_of_breweries_by_size(query)
    json_response = response.json()
    assert json_response
    assert response.status_code == code
    assert len(json_response) == size
    for brewery in json_response:
        assert brewery["id"] is not None
