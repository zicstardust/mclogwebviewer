import os

def logs_list(path_out):
    logs_list = os.listdir(path_out)
    if os.getenv('FLASK_DEBUG'):
        print(f'\nlogs_list:\n{logs_list}')
    return logs_list