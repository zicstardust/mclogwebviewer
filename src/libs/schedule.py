from datetime import datetime, timedelta
import os
import app


def datetime_to_str(date:datetime,format='%Y-%m-%d %H:%M:%S'):
    date_string = date.strftime(format)
    return date_string


def str_to_datetime(date_time:str,format='%Y-%m-%d %H:%M:%S'):
    datetime_str = datetime.strptime(date_time, format)
    return datetime_str


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



def schedule_isExpired():
    if app.schedule_interval == "0":
        return True
    
    elif (parser_interval(app.schedule_interval) == 0):
        print("Invalid internal, SCHEDULE_INTERVAL will be ignored")
        return True
    
    elif 'SCHEDULE_EXPIRE' in os.environ:
        date_now=datetime.now()
        date_env=str_to_datetime(os.getenv('SCHEDULE_EXPIRE'))

        if (date_now > date_env):
            os.environ["SCHEDULE_EXPIRE"] = datetime_to_str(parser_interval(app.schedule_interval))
            if os.getenv('FLASK_DEBUG'):
                print("Schedule expired!")
                print(f"New schedule will expire: {date_env}")
            return True
        
        else:
            if os.getenv('FLASK_DEBUG'):
                print(f"Schedule will expire: {date_env}")
            return False

    else:        
        if os.getenv('FLASK_DEBUG'):
            print("Schedule env not found, create now")
        os.environ["SCHEDULE_EXPIRE"] = datetime_to_str(parser_interval(app.schedule_interval))
        return True
