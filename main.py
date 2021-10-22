from datetime import datetime
import requests

# creating a user profile with pixela using post method

USERNAME = "your pixela Username"
TOKEN = "your pixela token"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# creating the graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# creating a pixel on the graph

today = datetime.now().strftime("%Y%m%d")

pixel_params = {
    "date": today,
    "quantity": input("How many hours did you code today?"),
}

# response = requests.post(url=f"{graph_endpoint}/graph1", json=pixel_params, headers=headers)
# print(response.text)

# updating an already created pixel with put method
update_params = {
    "quantity": "2.5"
}

# response = requests.put(url=f"{graph_endpoint}/graph1/{today}", json=update_params, headers=headers)
# print(response.text)

# deleting a pixel with date of today

# response = requests.delete(url=f"{graph_endpoint}/graph1/{today}", headers=headers)
# print(response.text)
