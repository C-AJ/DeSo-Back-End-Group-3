import requests
import os
import json
import requests
from bson.json_util import dumps
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from pymongo import MongoClient
from dotenv import load_dotenv


from nftClass import NFT
from WalletClass import Wallet

load_dotenv()
app = Flask(__name__)
CORS(app)
client = MongoClient(os.environ.get("MOGNODB_URI"))
db = client["deso-v0"]
app.config['CORS_HEADERS'] = 'content-type'

nfts = db["nfts"]
baseURL = "http://localhost:17001/api/v0"

@app.route("/")

def index():
    return "DeSo backend running"

@app.route("/api/get-exchange-rate")
def getExcangeRate():
    r = requests.get('http://localhost:17001/api/v0/get-exchange-rate') # where we running node
    #r = requests.get('https://api.github.com', auth=('user', 'pass'))

    #print(r) 
    r.status_code
    #print 
    #r.headers[content-type]
    
    return jsonify(r.jason())

def submitTransaction():
    if request.method == "TRANSACTION":
        r = requests.get("http://localhost:17001/api/v0/get-transaction")
        r.status_code
        print(r.json)
        return jsonify({"success": True})

def createNFT():
    if request.method == "CREATE":
          r = requests.get("http://localhost:17001/api/v0/create-nft")
          r.status_code
          print(r.json)
          return jsonify({"success": True})

def submitPost():
    if request.method == "POST":
          r = requests.get("http://localhost:17001/api/v0/submit-post")
          r.status_code
          print(r.json)
          return jsonify({"success": True})    

def main():
    #getRequests()
    wallet = Wallet() # needs amount
    nft = NFT() # needs value, newOwner, and currentOwner

    nft.processTransaction(wallet.amount) # after this call, transaction should be complete
    # am i overthinking python?

    return

#app.run(debug = True)
if __name__ == "__main__":
    main()