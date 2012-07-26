from flask import redirect, url_for, render_template, request, g
from model import app

import pusher
pusher.app_id = ''
pusher.key = ''
pusher.secret = ''


@app.before_request
def setup_function():
    g.pusher = pusher.Pusher()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/navigate")
def navigate():
    dest_url = request.args['destination_url']
    g.pusher['events'].trigger("go", {"url": dest_url})
    return ""
