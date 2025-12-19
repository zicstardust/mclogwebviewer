import shutil
import gzip
import os


def process_logs(dir_list,path_in,path_out,max_logs:int):
    
    for filename in os.listdir(path_out):
        file_path = os.path.join(path_out, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

    dir_list.reverse()
    i=1

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
                if max_logs != 0:
                    i=i-1

        if int(max_logs) != 0:
            if i == int(max_logs):
                break
            else:
                i=i+1
