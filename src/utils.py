import shutil
import gzip
import os

path_in = os.environ.get("LOGS_FOLDER_PATH", "/logs")
#path_in = "./logs"
#path_in = "/logs"
#path_out = "./processed_logs"
path_out = os.environ.get("PROCECESSED_LOGS_FOLDER_PATH", "/data")
#path_out = "/data"

if os.getenv('FLASK_DEBUG'):
    print(f'\npath_in={path_in}')
    print(f'path_out={path_out}\n')

dir_list = os.listdir(path_in)

def processed_logs():
    for f in dir_list:
        if f.endswith(".log.gz"):
            with gzip.open(f'{path_in}/{f}', 'rb') as file_in:
                with open(f'{path_out}/{f.replace('.log.gz', '.log')}', 'wb') as file_out:
                    shutil.copyfileobj(file_in, file_out)
                    if os.getenv('FLASK_DEBUG'):
                        print(f'unzip: {f}')
        elif f.endswith('latest.log'):
            shutil.copyfile(f'{path_in}/{f}', f'{path_out}/{f}')
            if os.getenv('FLASK_DEBUG'):
                print(f'copy: {f}')
        else:
            if os.getenv('FLASK_DEBUG'):
                print(f'ignored: {f}')


def logs_list():
    logs_list = os.listdir(path_out)
    if os.getenv('FLASK_DEBUG'):
        print(f'\nlogs_list:\n{logs_list}')
    return logs_list

def open_log(log_file):
    if os.getenv('FLASK_DEBUG'):
        print(f'\nOpen log: {log_file}')
    return open(log_file, "r")