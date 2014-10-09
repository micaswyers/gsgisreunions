from flask import Flask, render_template, request
import json
import os
import requests


app = Flask(__name__)
INITIAL_REQUEST_URL="https://api.instagram.com/v1/tags/frenchbulldog/media/recent?client_id=b1da9d7eeb1a4f638234ff7d846b008a"

def call_api(request=INITIAL_REQUEST_URL):
    r = requests.get(request)

    urls_list = map(lambda x: x['images']['standard_resolution']['url'], r.json()['data'])
    return urls_list

@app.route("/", )
def index():
    urls_list =  call_api()
    return render_template('index.html', urls_list=urls_list)

@app.route("/next", )
def get_more_images():
    pass

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

