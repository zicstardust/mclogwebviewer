from datetime import datetime, timedelta
import os


def parser_interval(interval:str):
    number=int(interval[:-1])
    operation=interval[-1:]

    if not isinstance(number, int):
        return 0

    if operation.upper() == 'S':
        time=timedelta(seconds=number)
    elif operation.upper() == 'M':
        time=timedelta(minutes=number)
    elif operation.upper() == 'H':
        time=timedelta(hours=number)
    elif operation.upper() == 'D':
        time=timedelta(days=number)
    elif operation.upper() == 'W':
        time=timedelta(weeks=number)
    else:
        return 0

    return datetime.now() + time


def datetime_to_str(date:datetime,format='%Y-%m-%d %H:%M:%S'):
    date_string = date.strftime(format)
    return date_string

def str_to_datetime(date_time:str,format='%Y-%m-%d %H:%M:%S'):
    datetime_str = datetime.strptime(date_time, format)
    return datetime_str


def datetime_to_file(date_time:datetime, path):
    if os.path.exists(f'{path}/datetime'):
        os.remove(f'{path}/datetime')

    date_str=datetime_to_str(date_time)
    with open(f'{path}/datetime', "w") as file:
        file.write(date_str)



def file_to_datetime(path):
    with open(f'{path}/datetime', "r") as f:
        file = f.readlines()
        res = ' '.join(file)
    return str_to_datetime(res)

def generate_file(interval, path):
    date_time=parser_interval(interval)
    datetime_to_file(date_time, path)
