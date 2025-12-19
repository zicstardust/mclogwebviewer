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