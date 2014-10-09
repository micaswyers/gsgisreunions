from flask import Flask, render_template, request
import json
import os
import requests


app = Flask(__name__)
INITIAL_REQUEST_URL="https://api.instagram.com/v1/tags/frenchbulldog/media/recent?client_id=b1da9d7eeb1a4f638234ff7d846b008a"
NEXT_URL = None
def call_api(request=INITIAL_REQUEST_URL):
    global NEXT_URL
    r = requests.get(request)
    NEXT_URL = r.json()['pagination']['next_url']
    urls_list = map(lambda x: x['images']['standard_resolution']['url'], r.json()['data'])

    return urls_list

@app.route("/", )
def index():
    urls_list =  call_api()
    return render_template('index.html', urls_list=urls_list)

@app.route("/next", methods=["GET"])
def get_more_images():
    urls_list = call_api(NEXT_URL)
    return json.dumps(
        {"urls": urls_list}
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

