from flask import Flask, render_template, request
import json
import requests


from secrets import CLIENT_ID

app = Flask(__name__)


r = requests.get("https://api.instagram.com/v1/tags/gsgisreunions/media/recent?client_id=%s" % CLIENT_ID)

urls_list = map(lambda x: x['images']['standard_resolution']['url'], r.json()['data'])


@app.route("/", )
def index():
    return render_template('index.html', urls_list = urls_list)


if __name__ == "__main__":
   app.run(debug=True)


