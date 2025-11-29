import shutil
import gzip
import os

def processed_logs(dir_list,path_in,path_out):
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


def logs_list(path_out):
    logs_list = os.listdir(path_out)
    if os.getenv('FLASK_DEBUG'):
        print(f'\nlogs_list:\n{logs_list}')
    return logs_list


def open_log(log_file):
    if os.getenv('FLASK_DEBUG'):
        print(f'\nOpen log: {log_file}')
    return open(log_file, "r")
