import requests
import os
token = os.getenv("HABIT_TRACKER_TOKEN")
username = os.getenv("HABIT_TRACKER_UN")
pixela_endpoint ='https://pixe.la/v1/users'
parameters = {'token':token,'username':username,'agreeTermsOfService':'yes','notMinor':'yes'}
# response = requests.post(url=pixela_endpoint,json=parameters)
# # response.raise_for_status()
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{username}/graphs/graph1'
graph_config = {
    'id':'graph1',
    'name':'coding graph',
    'unit':'hours',
    'type': 'float',
    'color':'ajisai'
}

headers = {'X-USER-TOKEN':token}
# response = requests.post(url = graph_endpoint,json=graph_config,headers=headers)
# print(response.text)
graph_update = {'date': '20241020','quantity': '1'}
response = requests.post(url=graph_endpoint,json=graph_update,headers=headers)
print(response.text)

