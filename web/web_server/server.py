from flask import Flask
import json
from firebase import firebase
from flask_cors import CORS, cross_origin
from flask import jsonify
from flask import request
from serverfunc import *

app = Flask(__name__)
CORS(app)
@app.route("/userAuth",methods = ['POST'])
def user_auth():
    # data = json.loads(request.data)
    data = json.loads(request.data)
    print data
    username = data["username"]
    password = data["password"]
    valid = login(username, password)
    if(valid):
      return jsonify({
      'status': '1'
      }
      ) 

    return jsonify({
      'status': '0'
      }
      ) 


if __name__ == "__main__":
	app.run(host='0.0.0.0')

