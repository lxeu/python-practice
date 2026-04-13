import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

sheety_endpoint = "https://api.sheety.co/46ac933003aef9e223b449c5eb74826a/flightDeals/prices"

class DataManager:
    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(sheety_endpoint, auth=self._authorization)
        data = response.json()
        return data["prices"]
    
    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        requests.put(
            url=f"{sheety_endpoint}/{row_id}",
            json=new_data,
            auth=self._authorization
        )