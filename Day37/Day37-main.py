import requests
from datetime import datetime

USERNAME = "lxeuu"
TOKEN = "aslkd32feskljf322"
GRAPHID = "graph1"
today = datetime.now()

pixela_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPHID,
    "name": "Coding Graph",
    "unit": "Hours",
    "type": "int",
    "color": "kuro",

}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response2 = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response2.json())

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_params, headers=headers)
print(response.text)