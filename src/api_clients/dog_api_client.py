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

    def get_single_random_image(self):
        response = self.session.get(url=f"{self.base_url}/image/random")
        return response

    def get_multiple_random_images(self, image_quantity):
        response = self.session.get(url=f"{self.base_url}/image/random/{image_quantity}")
        return response

    def get_single_random_sub_breed_image(self, sub_breed):
        self.base_url = "https://dog.ceo/api/breed/hound"
        response = self.session.get(url=f"{self.base_url}/{sub_breed}/images/random")
        return response

    def get_list_all_sub_breeds(self):
        self.base_url = "https://dog.ceo/api/breed/hound"
        response = self.session.get(url=f"{self.base_url}/list")
        return response

