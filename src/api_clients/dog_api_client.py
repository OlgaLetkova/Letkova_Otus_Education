import requests


class DogsApiClient():
    def __init__(self,
                 base_url="https://dog.ceo/api/breeds"):
        self.session = requests.Session()
        self.session.headers = {"Content-Type": "application/json"}
        self.session.verify = False
        self.base_url = base_url

    def get_list_all_breeds(self):
        response = self.session.get(url=f"{self.base_url}/list/all")
        return response

    def get_random_image(self):
        response = self.session.get(url=f"{self.base_url}/image/random")
        return response

    def get_multiple_random_images(self, query):
        response = self.session.get(url=f"{self.base_url}/image/random/{query}")

