import requests


class PlaceholderApiClient():
    def __init__(self,
                 base_url="https://jsonplaceholder.typicode.com/posts"):
        self.session = requests.Session()
        self.session.headers = {"Content-Type": "application/json; charset=UTF-8"}
        self.session.verify = False
        self.base_url = base_url

    def get_all_resources(self):
        response = self.session.get(url=f"{self.base_url}")
        return response

    def create_one_resource(self, data):
        response = self.session.post(url=f"{self.base_url}", json=data)
        return response

    def update_one_resource(self, data, resource_number):
        response = self.session.put(url=f"{self.base_url}/{resource_number}", json=data)
        return response

    def patch_one_resource(self, data, resource_number):
        response = self.session.patch(url=f"{self.base_url}/{resource_number}", json=data)
        return response

    def get_one_resource_by_id(self, resource_number):
        response = self.session.get(url=f"{self.base_url}/{resource_number}")
        return response
