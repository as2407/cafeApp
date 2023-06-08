from flask import Flask, request
import json
app = Flask(__name__)
base_url = '/api/v1'


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
    print(request_body)
    return 'successfully done!'


# Registration
@app.post(base_url + '/signup')
def signup():
    # firstname, lastname, email, password_hash
    request_body = json.loads(request.data)
    print(request_body)
    return 'signup'


if __name__ == '__main__':
    app.run()
