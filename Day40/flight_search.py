import os
import requests
from dotenv import load_dotenv

load_dotenv()
SERP_API_ENDPOINT = "https://serpapi.com/search"

class FlightSearch:
    def __init__(self):
        self._api_key = os.environ["SERP_API_KEY"]

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):
        query = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "currency": "CAD",
            "api_key": self._api_key,
        }

        if is_direct:
            query["stops"] = "0"
        else:
            query["stops"] = "1"


        response = requests.get(SERP_API_ENDPOINT, params=query)
        response.raise_for_status()
        return response.json()

