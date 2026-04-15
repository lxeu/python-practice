class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, airline, flight_number, stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.airline = airline
        self.flight_number = flight_number
        self.stops = stops


def find_cheapest_flight(data, return_date):
    if data is None or (not data.get("best_flights") and not data.get("other_flights")):
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", 0)

    all_flights = data.get("best_flights", []) + data.get("other_flights", [])

    first_flight = all_flights[0]
    lowest_price = first_flight["price"]

    first_leg = first_flight["flights"][0]

    origin = first_leg["departure_airport"]["id"]
    destination = first_flight["flights"][-1]["arrival_airport"]["id"]
    out_date = first_leg["departure_airport"]["time"].split(" ")[0]

    airline = first_leg.get("airline", "N/A")
    flight_number = first_leg.get("flight_number", "N/A")

    nr_stops = len(first_flight["flights"]) - 1

    cheapest_flight = FlightData(
        lowest_price,
        origin,
        destination,
        out_date,
        return_date,
        airline,
        flight_number,
        nr_stops,
    )

    for flight in all_flights:
        try:
            price = flight["price"]
        except KeyError:
            print("--- No price available for flight. ---")
            continue

        if price < lowest_price:
            lowest_price = price

            first_leg = flight["flights"][0]

            origin = first_leg["departure_airport"]["id"]
            destination = flight["flights"][-1]["arrival_airport"]["id"]
            out_date = first_leg["departure_airport"]["time"].split(" ")[0]

            airline = first_leg.get("airline", "N/A")
            flight_number = first_leg.get("flight_number", "N/A")

            cheapest_flight = FlightData(
                lowest_price,
                origin,
                destination,
                out_date,
                return_date,
                airline,
                flight_number,
                nr_stops,
            )

            print(f"Lowest price to {destination} is CAD {lowest_price}")

    return cheapest_flight