from flask import Flask, request

import sys
import json

sys.path.append("config")
sys.path.append("controller")
from config import firebase_config
from controller import auth_controller

app = Flask(__name__)
base_url = '/api/v1'

firebase_config_object = firebase_config.FirebaseConfig()


# GET: return Response Data (JSON/HTML/XML)
# POST: when we want to SEND DATA to server and usually used to CREATE stuff
# PUT / PATCH: UPDATE stuff
# DELETE: is to REMOVE stuff

@app.get('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# Login
@app.post(base_url + '/signin')
def signin():
    # using request(object) to get the hidden data which is imported from flask
    request_body = json.loads(request.data)
    auth_controller.sign_in(firebase_config_object, request_body['email'], request_body['password'])
    return 'successfully done!'


# Registration
@app.post(base_url + '/signup')
def signup():
    # firstname, lastname, email, password_hash
    request_body = json.loads(request.data)
    # print(request_body)
    auth_controller.sign_up(firebase_config_object, request_body['firstname'], request_body['lastname'], request_body['email'], request_body['password'])
    return 'signup'


if __name__ == '__main__':
    print(firebase_config_object)
    app.run()
