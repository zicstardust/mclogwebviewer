import os
from flask import Flask, redirect, url_for
from libs.get_icon import get_icon
from routes.index import index_bp


if os.getenv('FLASK_DEBUG'):
    from dotenv import load_dotenv
    load_dotenv()

app = Flask(__name__)
app.register_blueprint(index_bp)

path_in = '/logs'
path_out = '/data'
icon_path = os.environ.get("ICON", './server-icon.png')
max_logs = os.environ.get("MAX_LOGS", 0)
hide_github_icon=os.environ.get("HIDE_GITHUB_ICON", False)
app_title=os.environ.get("APP_TITLE", "MC Log Web Viewer")
filter_text=os.environ.get("FILTER_TEXT", '')
schedule_interval=os.environ.get("SCHEDULE_INTERVAL", "0")


#Error 404
@app.errorhandler(404)
def not_found(e):
    return redirect(url_for('index.index'))
    
    
os.environ["ICON"] = get_icon(icon=icon_path,static_dir=app.static_folder)


if os.getenv('FLASK_DEBUG'):
    print('=========FLASK_DEBUG==========')

    print(f'MAX_LOGS: {max_logs}')
    print(f'path_in={path_in}')
    print(f'path_out={path_out}')
    print(f'hide_github_icon={hide_github_icon}')
    
    print('==============================')
