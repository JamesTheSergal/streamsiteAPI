import requests

BASE = "http://5.161.219.150:5000/"

#response = requests.get(BASE + "makeStreamKey")
#print(response.json())

response = requests.post(BASE + "verifyStreamKey", params={"name": "dd624955-5570-4b15-9135-0cdfed2debb1"})
print(response.json())