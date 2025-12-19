import os
from flask import Flask, redirect, render_template, request, url_for
from os.path import exists
from libs.logs_list import logs_list
from libs.open_log import open_log
from libs.process_logs import process_logs
from libs.set_icon import set_icon



if os.getenv('FLASK_DEBUG'):
    from dotenv import load_dotenv
    load_dotenv()


path_in = "/logs"
path_out = "/data"
hide_github_icon = os.environ.get("HIDE_GITHUB_ICON", False)
max_logs = os.environ.get("MAX_LOGS", 0)


app = Flask(__name__)


set_icon(static_dir=app.static_folder)


if os.getenv('FLASK_DEBUG'):
    print('=========FLASK_DEBUG==========')
    
    path_in = os.environ.get("LOGS_FOLDER_PATH", path_out)
    path_out = os.environ.get("PROCECESSED_LOGS_FOLDER_PATH", path_out)

    print(f'MAX_LOGS: {max_logs}')
    print(f'path_in={path_in}')
    print(f'path_out={path_out}')
    print(f'hide_github_icon={hide_github_icon}')
    
    print('==============================')

@app.route("/")
def index():   
    dir_list = os.listdir(path_in)
    process_logs(dir_list=dir_list,
                   path_in=path_in,
                   path_out=path_out,
                   max_logs=max_logs
                   )
    date = request.args.get('date', default = "latest")
    app_title = os.environ.get("APP_TITLE", "MC Log Web Viewer")
    log = open_log(f'{path_out}/{date}.log')
    log_list = logs_list(path_out=path_out)
    return render_template("index.html",
                           log=log,
                           date=date,
                           log_list=log_list,
                           hide_github_icon=hide_github_icon,
                           app_title=app_title
                           )


@app.errorhandler(404)
def not_found(e):
    return redirect(url_for('index'))
