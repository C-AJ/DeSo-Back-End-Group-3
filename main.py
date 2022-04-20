from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    r = requests.get('http://localhost:17001/api/v0/get-exchange-rate')
    
    return r.text
    
app.run(debug = True)
