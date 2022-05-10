from urllib import response
import requests
import os
import json
from bson.json_util import dumps
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'content-type'

# DeSo Node
NODE_DESO = "https://node.deso.org"

# Deso Local Node
NODE_LOCAL = "http://localhost:" + str(os.environ.get("DESO_PORT"))
baseURL = NODE_DESO + "/api"

PRODUCTION = os.environ.get("PRODUCTION")
PORT = 8080 if PRODUCTION else 17000

headers = {
  "Content-Type": "application/json"
}

@app.route("/")
def index():
    return "DeSo backend running"

@app.route("/api/get-exchange-rate") # mostly for checking server connection stuff
def getExchangeRate():
    r = requests.get("http://localhost:17001/api/v0/get-exchange-rate")
    return jsonify(r.json())      

# so these functions have the base code for the tasks listed on the "all hands" doc
# they most likely are not finished and need extra things so we can forward info to frontend (i believe that's what we're doing)
# cannot test until we get the proxy server going though
@app.route("/api/submit-transaction", methods=["POST"])
def submitTransaction():
    if request.method == "POST":
        print(request.json)
        payload = json.dumps(request.json)
        headers = {
            "Content-Type": "application/json"
        }
        r = requests.post("http://localhost:17001/api/v0/transaction", data=request.json)
        return jsonify(r.json())

@app.route("/api/create-nft", methods=["POST"])
def createNFT():
    if request.method == "POST":
        print(request.json)
        payload = json.dumps(request.json)
        headers = {
            "Content-Type": "application/json"
        }
        r = requests.post("http://localhost:17001/api/v0/nft", data=request.json)
        return jsonify(r.json())

@app.route("/api/submit-post", methods=["POST"])
def submit_post():
  if request.method == "POST":
    print(request.json)
    payload = json.dumps(request.json)
    headers = {
      "Content-Type": "application/json"
    }
    post = requests.post("http://localhost:17001/api/v0/submit-post", headers=headers ,data=payload)
    print(post.json())
    return jsonify(post.json())    

app.run(debug = True)