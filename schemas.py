schema_list_all = {
    "type": "object",
    "properties": {
        "message": {"type": "object"},
        "status": {"type": "string"}
    }
}

schema_one_dog = {
    "type": "object",
    "properties": {
        "message": {"type": "string"},
        "status": {"type": "string"}
    }
}

schema_list_all_sub_breeds = {
    "type": "object",
    "properties": {
        "message": {"type": "array"},
        "status": {"type": "string"}
    }
}

schema_one_brewery = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "brewery_type": {"type": "string"},
        "address_1": {"type": "string"},
        "address_2": {"type": "null"},
        "address_3": {"type": "null"},
        "city": {"type": "string"},
        "state_province": {"type": "string"},
        "postal_code": {"type": "string"},
        "country": {"type": "string"},
        "longitude": {"type": "string"},
        "latitude": {"type": "string"},
        "phone": {"type": "string"},
        "website_url": {"type": "string"},
        "state": {"type": "string"},
        "street": {"type": "string"}
    }
}

schema_one_resource = {
    "type": "object",
    "properties": {
        "id": {"type": 'number'},
        "title": {"type": "string"},
        "body": {"type": "string"},
        "userId": {"type": 'number'}
    }
}
