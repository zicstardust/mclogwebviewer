import os

def logs_list(path_out):
    logs_list = []
    logs_dir = os.listdir(path_out)
    if os.getenv('FLASK_DEBUG'):
        print(f'\nlogs_list:\n{logs_dir}')
    for f in logs_dir:
        logs_list.append(f.replace(".log", ""))
    logs_list.reverse()
    return logs_list