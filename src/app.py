import os
from flask import Flask, render_template, request, url_for
from os.path import exists
from utils import logs_list, open_log, processed_logs


if exists('./.env'):
    from dotenv import load_dotenv
    load_dotenv()


path_in = os.environ.get("LOGS_FOLDER_PATH", "/logs")
path_out = os.environ.get("PROCECESSED_LOGS_FOLDER_PATH", "/data")


app = Flask(__name__)


if exists(f'{app.static_folder}/server-icon.png'):
    server_icon=True
else:
    server_icon=False


@app.route("/")
def index():
    if os.getenv('FLASK_DEBUG'):
        print(f'\npath_in={path_in}')
        print(f'path_out={path_out}\n')
        print(f'server_icon={server_icon}\n')
    
    dir_list = os.listdir(path_in)
    processed_logs(dir_list=dir_list,path_in=path_in,path_out=path_out)
    date = request.args.get('date', default = "latest.log")
    log = open_log(f'{path_out}/{date}')
    log_list = logs_list(path_out=path_out)
    return render_template("index.html", log=log, date=date, log_list=log_list, server_icon=server_icon)
