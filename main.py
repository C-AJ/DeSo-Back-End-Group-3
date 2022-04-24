from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def getRequests():
    r = requests.get('http://localhost:17001/api/v0/get-exchange-rate')
    r = requests.get('https://api.github.com', auth=('user', 'pass'))

    print 
    r.status_code
    print 
    r.headers[content-type]
    
    return r.text

def processTransaction():


    print("NFT Transaction Processing")

app.run(debug = True)