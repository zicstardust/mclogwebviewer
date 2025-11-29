from flask import Flask, render_template, request
from os.path import exists
from utils import logs_list, open_log, processed_logs


if exists('./.env'):
    from dotenv import load_dotenv
    load_dotenv()


app = Flask(__name__)

@app.route("/")
def index():
    processed_logs()
    date = request.args.get('date', default = "latest.log")
    log = open_log(f'./processed_logs/{date}')
    log_list = logs_list()
    return render_template("index.html", log=log, date=date, log_list=log_list)
