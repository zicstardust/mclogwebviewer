import app
from libs.copy_logs import copy_logs
from libs.filter_logs import filter_logs

def log_generator():
    
    copy_logs(path_in=app.path_in,
              path_out=app.path_out,
              max_logs=app.max_logs)

    filter_logs(path_out=app.path_out, filter=app.filter_text)
