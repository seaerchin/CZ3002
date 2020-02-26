from google.cloud import firestore
import os 
from flask import Flask
from flask import redirect, url_for, request, make_response, jsonify, render_template
from google.cloud import storage
import requests  
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "private.json"

# Project ID is determined by the GCLOUD_PROJECT environment variable
# persistent object passed around 
db = firestore.Client()

# register default configs and blueprints 

app = Flask(__name__)
app.config.from_pyfile("config.py")
app.register_blueprint(cloudFireStore.crud)


@app.route('/')
def hello() -> str:
    return "hello world"

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)