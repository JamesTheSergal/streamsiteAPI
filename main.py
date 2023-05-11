import os
from dotenv import load_dotenv
from flask import Flask, abort, jsonify, request
from flask_restful import Api, Resource
import uuid
import mysql.connector

# Check to see if .env exists
if not os.path.isfile(".env"):
    print("No enviroment file found to run the server...")
    exit()

# Load the enviroment file
load_dotenv()
print("Loaded enviroment file...")

mysql_host = os.getenv("mysql_host")
mysql_user = os.getenv("mysql_user")
mysql_password = os.getenv("mysql_pass")

# Connect to the database
db = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database="streamagent"
)

print("Connected to database..."")

app = Flask(__name__)
api = Api(app)

streams = []

streams.append("snerg")

def abortKeyNotValid():
    # Abort the request if the key is not valid
    abort(401, "Key not valid")

class MakeStreamKey(Resource):
    def get(self):
        # Return Json for a randomized id
        id = str(uuid.uuid4())
        streams.append(id)
        print(f'Stream keys: ')
        print(streams)
        return jsonify({"id": id})
    
class verifyStreamKey(Resource):
    def post(self):
        splitdata = {}
        # Verify that the stream key is valid
        postdata = request.get_data()
        postdata = str(postdata.decode("utf-8")).split("&")
        for i in range(len(postdata)):
            key = postdata[i].split("=")[0]
            data = postdata[i].split("=")[1]
            splitdata[key] = data

        if splitdata["name"] in streams:
            return jsonify({"valid": True})
        else:
            abortKeyNotValid()
        pass

class greetTraveler(Resource):
    def get(self):
        return "Hello traveler!"

api.add_resource(verifyStreamKey, "/verifyStreamKey") 
api.add_resource(MakeStreamKey, "/makeStreamKey")
api.add_resource(greetTraveler, "/")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)