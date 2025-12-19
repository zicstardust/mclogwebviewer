import os
import shutil
from urllib.request import urlretrieve

url='https://images.icon-icons.com/1381/PNG/512/minecraft_94415.png'

def set_icon(static_dir,
             default_icon=url,
             path_icon=os.environ.get("GET_ICON_PATH", '/server-icon.png')):
    if os.path.exists(f'{static_dir}/server-icon'):
        os.remove(f'{static_dir}/server-icon')

    if os.path.exists(path_icon):
        if os.getenv('FLASK_DEBUG'):
            print(f"Copy \"{path_icon}\"")
        shutil.copyfile(path_icon, f'{static_dir}/server-icon')
    else:
        if os.getenv('FLASK_DEBUG'):
            print("Downloding default icon")
        urlretrieve(default_icon, f'{static_dir}/server-icon')