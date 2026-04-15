import requests_cache
from pprint import pprint
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()
pprint(sheet_data)

data_manager.destination_data = sheet_data

customer_data = data_manager.get_customer_emails()
customer_email_list = [row["email"] for row in customer_data]

ORIGIN_CITY_IATA = "YEG"

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")

    best_price = float("inf")
    best_flight = None

    for i in range(0, 180, 6):
        departure_date = datetime.now() + timedelta(days=i)
        return_date = departure_date + timedelta(days=7)

        flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=departure_date,
            to_time=return_date
        )

        cheapest_flight = find_cheapest_flight(
            flights,
            return_date=return_date.strftime("%Y-%m-%d")
        )

        if cheapest_flight.price != "N/A" and cheapest_flight.price < best_price:
            best_price = cheapest_flight.price
            best_flight = cheapest_flight

    if best_flight and best_flight.price < destination["lowestPrice"]:
        
        if best_flight.stops == 0:
            message = (f"Low price alert! Only CAD {best_flight.price} to fly direct "
                       f"from {best_flight.origin_airport} to {best_flight.destination_airport}, "
                       f"on {best_flight.out_date} until {best_flight.return_date}.")
        else:
            message = (f"Low price alert! Only CAD {best_flight.price} to fly "
                       f"from {best_flight.origin_airport} to {best_flight.destination_airport}, "
                       f"with {best_flight.stops} stop(s) "
                       f"departing on {best_flight.out_date} and returning on {best_flight.return_date}.")

        print(f"BEST DEAL FOUND: {destination['city']} - CAD {best_flight.price}")
        print(f"Check your email. Lower price flight found to {destination['city']}!")

        notification_manager.send_emails(email_list=customer_email_list, email_body=message)