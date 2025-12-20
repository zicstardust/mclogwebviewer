import os
from flask import Flask, redirect, url_for
from libs.set_icon import set_icon
from routes.index import index_bp


if os.getenv('FLASK_DEBUG'):
    from dotenv import load_dotenv
    load_dotenv()


path_in = "/logs"
path_out = "/data"
max_logs = os.environ.get("MAX_LOGS", 0)
hide_github_icon=os.environ.get("HIDE_GITHUB_ICON", False),
app_title=os.environ.get("APP_TITLE", "MC Log Web Viewer")
filter_text=os.environ.get("FILTER_TEXT", '')

app = Flask(__name__)
app.register_blueprint(index_bp)

#Error 404
@app.errorhandler(404)
def not_found(e):
    return redirect(url_for('index.index'))
    

#app.register_blueprint(error404_bp)

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
