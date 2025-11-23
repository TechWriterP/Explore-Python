import requests
from datetime import datetime


USERNAME="rpaprashant"
TOKEN="s3cureT0ken!"

pixela_endpoint = "https://pixe.la/v1/users"

user_params ={
    "token":TOKEN ,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graphs_config ={
    "id":"graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN":TOKEN
}

requests.post(url=graph_endpoint,json=graphs_config, headers=headers)

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
today = datetime.today()
post_pixel_config = {
    "date":today.strftime("%Y%m%d"),
    "quantity": "10.5"
}

# pixel_response = requests.post(url=post_pixel_endpoint, json=post_pixel_config, headers=headers)
# print(pixel_response.text)

update_pixela_endpoint = f"{post_pixel_endpoint}/{today.strftime("%Y%m%d")}"
update_pixel_config = {
    "quantity": "20"
}

update_pixela_response = requests.put(url=update_pixela_endpoint, json=update_pixel_config, headers=headers)
print(update_pixela_response.text)