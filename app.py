from flask import Flask, render_template, request
import json
import os
import requests

CLIENT_ID = os.environ['CLIENT_ID']

app = Flask(__name__)
INITIAL_REQUEST_URL="https://api.instagram.com/v1/tags/frenchbulldog/media/recent?client_id=%s" % CLIENT_ID
NEXT_URL = None
def call_api(request=INITIAL_REQUEST_URL):
    global NEXT_URL
    r = requests.get(request)
    if 'next_url' in r.json()['pagination'].keys():
        NEXT_URL = r.json()['pagination']['next_url']
    else:
        NEXT_URL = False
    urls_list = map(lambda x: x['images']['standard_resolution']['url'], r.json()['data'])

    return urls_list

@app.route("/", )
def index():
    urls_list =  call_api()
    if NEXT_URL:
        is_next = True
    else:
        is_next = False

    return render_template('index.html', urls_list=urls_list, is_next=is_next)

@app.route("/next", methods=["GET"])
def get_more_images():
    urls_list = call_api(NEXT_URL)
    return json.dumps(
        {"urls": urls_list}
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

