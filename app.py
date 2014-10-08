from flask import Flask, render_template, request
import json
import os
import requests


app = Flask(__name__)
INITIAL_REQUEST_URL="https://api.instagram.com/v1/tags/gsgisreunions/media/recent?client_id=b1da9d7eeb1a4f638234ff7d846b008a"
NEXT_URL = None

def call_api(request=INITIAL_REQUEST_URL):
    r = requests.get(request)
    global NEXT_URL
    NEXT_URL = r.json()['pagination']['next_url']
    return map(lambda x: x['images']['standard_resolution']['url'], r.json()['data'])

@app.route("/", )
def index():
    urls_list =  call_api()
    return render_template('index.html', urls_list=urls_list)

@app.route("/next", )
def get_more_images():
    global NEXT_URL
    urls_list = call_api(NEXT_URL)
    return render_template('index.html', urls_list=urls_list)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

