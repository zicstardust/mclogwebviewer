from flask import Blueprint, render_template, request
import app
from libs.open_log import open_log
from libs.log_generator import log_generator
from libs.logs_list import logs_list
from libs.schedule import schedule_isExpired

index_bp = Blueprint('index', __name__)

@index_bp.route("/",  methods=['GET'])
def index():   

    if schedule_isExpired():
        log_generator()

    log_list=logs_list(app.path_out)
    date = request.args.get('date', default = "latest")
    log = open_log(f'{app.path_out}/{date}.log')

    return render_template("index.html",
                           log=log,
                           date=date,
                           log_list=log_list,
                           hide_github_icon=app.hide_github_icon,
                           app_title=app.app_title
                           )


