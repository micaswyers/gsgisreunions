from flask import Flask, render_template, request
import json
import requests



app = Flask(__name__)


r = requests.get("https://api.instagram.com/v1/tags/gsgisreunions/media/recent?client_id=b1da9d7eeb1a4f638234ff7d846b008a")

urls_list = map(lambda x: x['images']['standard_resolution']['url'], r.json()['data'])


@app.route("/", )
def index():
    return render_template('index.html', urls_list = urls_list)


if __name__ == "__main__":
   app.run(debug=True)


