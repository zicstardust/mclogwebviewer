import os

def open_log(log_file):
    if os.getenv('FLASK_DEBUG'):
        print(f'\nOpen log: {log_file}')
    return open(log_file, "r")
