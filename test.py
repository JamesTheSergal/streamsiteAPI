import requests
import os
from dotenv import load_dotenv

# Check to see if .env exists
if not os.path.isfile(".env"):
    print("No enviroment file found to run the server...")
    exit()

# Load the enviroment file
load_dotenv()

BASE = os.environ.get("api_url")

#response = requests.get(BASE + "makeStreamKey")
#print(response.json())

response = requests.post(BASE + "verifyStreamKey", params={"name": "dd624955-5570-4b15-9135-0cdfed2debb1"})
print(response.json())