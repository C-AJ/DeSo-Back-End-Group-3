from urllib import response
import requests
import os
import json
from bson.json_util import dumps
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'content-type' # using this base url bc this is where our node is

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
        r = requests.post("http://localhost:17001/api/v0/transaction", data=request.json)
        return jsonify(r.json())

@app.route("/api/create-nft", methods=["POST"])
def createNFT():
    if request.method == "POST":
        print(request.json)
        r = requests.post("http://localhost:17001/api/v0/nft", data=request.json)
        return jsonify(r.json())

@app.route("/api/submit-post", methods=["POST"])
def submitPost():
    if request.method == "POST":
        print(request.json)
        r = requests.post("http://localhost:17001/api/v0/post", data=request.json)
        headers = {'Accept': 'application/json'} # trying to fix JSONDecodeError
        response = requests.get("http://localhost:17001/api/v0/post", headers=headers).json()
        return jsonify(r.json()) 
        #return jsonify({"success":True}) # debug line

app.run(debug = True)