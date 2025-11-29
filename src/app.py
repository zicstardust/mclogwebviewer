from flask import Flask, render_template, request
from lib.open_log import open_log

app = Flask(__name__)

@app.route("/")
def index():
    date = request.args.get('date', default = "latest")
    log = open_log("/home/zic/Downloads/Nova pasta/logs/latest.log")
    return render_template("index.html", log=log, date=date)