import requests


class BreweryApiClient():
    def __init__(self,
                 base_url="https://api.openbrewerydb.org/v1/breweries"):
        self.session = requests.Session()
        self.session.headers = {"Content-Type": "application/json"}
        self.session.verify = False
        self.base_url = base_url

    def get_single_brewery_by_id(self, _id):
        response = self.session.get(url=f"{self.base_url}/{_id}")
        return response

    def get_brewery_by_city(self, query):
        response = self.session.get(url=f"{self.base_url}",
                                    params=query)
        return response

    def get_brewery_by_state(self, query):
        response = self.session.get(url=f"{self.base_url}",
                                    params=query)
        return response

    def get_brewery_by_ids(self, query):
        response = self.session.get(url=f"{self.base_url}",
                                    params=query)
        return response

    def get_number_of_breweries_by_size(self, query):
        response = self.session.get(url=f"{self.base_url}/random",
                                    params=query)
        return response
