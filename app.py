from flask import Flask, render_template, request
import json
import os
import requests


NEXT_URL = None
app = Flask(__name__)

@app.route("/", )
def index():
    r = requests.get("https://api.instagram.com/v1/tags/frenchbulldog/media/recent?client_id=b1da9d7eeb1a4f638234ff7d846b008a")

    urls_list = map(lambda x: x['images']['standard_resolution']['url'], r.json()['data'])
    global NEXT_URL
    print "THIS IS THE NEXT URL"
    NEXT_URL = r.json()['pagination']['next_url']
    print NEXT_URL
    return render_template('index.html', urls_list = urls_list)

@app.route("/next", )
def get_more_images():
    r = requests.get(NEXT_URL)
    print "NOW THIS IS NEXT URL"
    print r.json()['pagination']['next_url']
    global NEXT_URL
    NEXT_URL = r.json()['pagination']['next_url']
    urls_list = map(lambda x: x['images']['standard_resolution']['url'], r.json()['data'])
    return render_template('index.html', urls_list = urls_list)





if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

