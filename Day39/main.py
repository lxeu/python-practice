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

    cheapest_flight = find_cheapest_flight(flights, return_date=six_month_from_today.strftime("%Y-%m-%d"))
    pprint(f"{destination['city']}: CAD {cheapest_flight.price}")

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(
            f"Lower price flight found to {destination['city']}! "
            f"From {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
            f"Airline: {airline}\n"
            f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}"
        )
        data_manager.update_lowest_price(destination["id"], cheapest_flight.price)