from flask import Flask, abort, jsonify, request
from flask_restful import Api, Resource
import uuid

app = Flask(__name__)
api = Api(app)

streams = []

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
        # Verify that the stream key is valid
        postdata = request.get_data()
        postdata = str(postdata.decode("utf-8")).split("&")
        print(postdata)

        #if key in streams:
        #    return jsonify({"valid": True})
        #else:
        #    abortKeyNotValid()
        pass
        

api.add_resource(verifyStreamKey, "/verifyStreamKey") 
api.add_resource(MakeStreamKey, "/makeStreamKey")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")