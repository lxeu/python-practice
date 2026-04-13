import requests_cache
from pprint import pprint
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight

requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_destination_data()
pprint(sheet_data)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

ORIGIN_CITY_IATA = "YEG"

for destination in sheet_data:
    pprint(f"Getting flights for {destination['city']}...")

    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    cheapest_flight = find_cheapest_flight(
        flights,
        return_date=six_month_from_today.strftime("%Y-%m-%d")
    )

    pprint(f"{destination['city']}: CAD {cheapest_flight.price}")

    if isinstance(cheapest_flight.price, (int, float)) and cheapest_flight.price < destination["lowestPrice"]:
        print(
            f"DEAL FOUND!!\n"
            f"{destination['city']} - CAD {cheapest_flight.price}\n"
            f"{cheapest_flight.origin_airport} → {cheapest_flight.destination_airport}\n"
            f"Airline: {cheapest_flight.airline}\n"
            f"Flight #: {cheapest_flight.flight_number}\n"
            f"{cheapest_flight.out_date} → {cheapest_flight.return_date}\n"
        )

        data_manager.update_lowest_price(
            destination["id"],
            cheapest_flight.price
        )