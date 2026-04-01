import requests
from twilio.rest import Client
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

will_rain = False
phone1 = os.environ.get("PHONE1")
phone2 = os.environ.get("PHONE2")
recipients = [phone2]

# BC
weather_params = {
    "lat": 49.282730,
    "lon": -123.120735,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()

# print(data["list"][0]["weather"][0]["id"])
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 600:
        will_rain = True
        break

if will_rain:
    for number in recipients:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        messaging_service_sid='MG0aa8a4c577fe5093e5aec794b2614ab0',
        body="It might rain today. Remember to bring an Umbrella!!",
        to=number
        )  
        print(message.sid)