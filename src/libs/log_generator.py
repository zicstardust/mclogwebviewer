import app
from libs.copy_logs import copy_logs
from libs.logs_list import logs_list

def log_generator():
    copy_logs(path_in=app.path_in,
              path_out=app.path_out,
              max_logs=app.max_logs)    
    return logs_list(path_out=app.path_out)