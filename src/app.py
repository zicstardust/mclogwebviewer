import os
from flask import Flask, render_template, request
from os.path import exists
from libs.logs_list import logs_list
from libs.open_log import open_log
from libs.processed_logs import processed_logs



if os.getenv('FLASK_DEBUG'):
    from dotenv import load_dotenv
    load_dotenv()


path_in = "/logs"
path_out = "/data"
hide_github_icon = os.environ.get("HIDE_GITHUB_ICON", False)

if os.getenv('FLASK_DEBUG'):
    path_in = os.environ.get("LOGS_FOLDER_PATH", path_out)
    path_out = os.environ.get("PROCECESSED_LOGS_FOLDER_PATH", path_out)

app = Flask(__name__)


if exists(f'{app.static_folder}/server-icon.png'):
    server_icon=True
else:
    server_icon=False


@app.route("/")
def index():
    if os.getenv('FLASK_DEBUG'):
        print(f'\npath_in={path_in}')
        print(f'path_out={path_out}')
        print(f'server_icon={server_icon}')
        print(f'hide_github_icon={hide_github_icon}\n')
    
    dir_list = os.listdir(path_in)
    processed_logs(dir_list=dir_list,path_in=path_in,path_out=path_out)
    date = request.args.get('date', default = "latest.log")
    log = open_log(f'{path_out}/{date}')
    log_list = logs_list(path_out=path_out)
    return render_template("index.html",
                           log=log,
                           date=date,
                           log_list=log_list,
                           server_icon=server_icon,
                           hide_github_icon=hide_github_icon
                           )
