import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

appid = os.getenv("NUTRITION_APPID")
api_key = os.getenv("NUTRITION_APIKEY")

exercise_text = input("Tell us what you did today: ")

nutrition_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheety_endpoint = "https://api.sheety.co/46ac933003aef9e223b449c5eb74826a/workoutTracking/workouts"

nutrition_params = {
    "query": exercise_text
}

headers = {
    "x-app-id": appid,
    "x-app-key": api_key,
}

response = requests.post(nutrition_endpoint, json=nutrition_params, headers=headers)
response.raise_for_status()
result = response.json()

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, auth=(os.getenv("NUTRITION_USER"), os.getenv("NUTRITION_PASS")))
