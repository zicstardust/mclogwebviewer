import os
import shutil

def get_icon(icon, static_dir):

    if os.path.exists(icon):
        if os.path.exists(f'{static_dir}/custom-server-icon'):
            os.remove(f'{static_dir}/custom-server-icon')
        shutil.copyfile(icon, f'{static_dir}/custom-server-icon')
        return "custom-server-icon"
    else:
        return "server-icon.png"
