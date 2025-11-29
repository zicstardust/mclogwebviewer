import os
from flask import Flask, render_template, request
from os.path import exists
from utils import logs_list, open_log, processed_logs



if exists('./.env'):
    from dotenv import load_dotenv
    load_dotenv()


path_in = os.environ.get("LOGS_FOLDER_PATH", "/logs")
path_out = os.environ.get("PROCECESSED_LOGS_FOLDER_PATH", "/data")


app = Flask(__name__)

@app.route("/")
def index():
    if os.getenv('FLASK_DEBUG'):
        print(f'\npath_in={path_in}')
        print(f'path_out={path_out}\n')
    
    dir_list = os.listdir(path_in)
    processed_logs(dir_list=dir_list,path_in=path_in,path_out=path_out)
    date = request.args.get('date', default = "latest.log")
    log = open_log(f'{path_out}/{date}')
    log_list = logs_list(path_out=path_out)
    return render_template("index.html", log=log, date=date, log_list=log_list)
