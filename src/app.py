from flask import Flask, render_template, request
from lib.utils import logs_list, open_log, processed_logs


processed_logs()

app = Flask(__name__)

@app.route("/")
def index():
    date = request.args.get('date', default = "latest.log")
    log = open_log(f'./processed_logs/{date}')
    log_list = logs_list()
    return render_template("index.html", log=log, date=date, log_list=log_list)