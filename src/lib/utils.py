import shutil
import gzip
import os

path_in = "./logs"
#path_in = "/logs"
path_out = "./processed_logs"
#path_out = "/data"
dir_list = os.listdir(path_in)

def processed_logs():
    for f in dir_list:
        if f.endswith(".log.gz"):
            with gzip.open(f'{path_in}/{f}', 'rb') as file_in:
                with open(f'{path_out}/{f.replace('.log.gz', '.log')}', 'wb') as file_out:
                    shutil.copyfileobj(file_in, file_out)
                    print(f'unzip: {f}')
        elif f.endswith('latest.log'):
            shutil.copyfile(f'{path_in}/{f}', f'{path_out}/{f}')
            print(f'copy: {f}')
        else:
            print(f'ignored: {f}')


def logs_list():
    return os.listdir(path_out)

def open_log(log_file):
    return open(log_file, "r")