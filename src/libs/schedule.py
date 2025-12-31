from datetime import datetime
import os
from libs.schedule_utils import file_to_datetime, generate_file, parser_interval
import app

def schedule_isExpired():

    if app.schedule_interval == "0":
        return True
    elif (parser_interval(app.schedule_interval) == 0):
        print("Invalid internal, SCHEDULE_INTERVAL will be ignored")
        return True
    elif os.path.exists('/tmp/mclogdatetime'):
        date_now=datetime.now()
        date_file=file_to_datetime()
        if (date_now > date_file):
            generate_file(app.schedule_interval)
            if os.getenv('FLASK_DEBUG'):
                print("Schedule expired!")
                print(f"New schedule will expire: {file_to_datetime()}")
            return True
        else:
            if os.getenv('FLASK_DEBUG'):
                print(f"Schedule will expire: {file_to_datetime()}")
            return False
    else:
        if os.getenv('FLASK_DEBUG'):
            print("Schedule file not found, create now")
        generate_file(interval=app.schedule_interval)
        return True