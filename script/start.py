import os

import time


def start_web_app():
    os.system("cd /opt/unusualWeather/")
    os.system(". venv/bin/activate")
    os.system("uwsgi uwsgi.ini")
    # time.sleep(1)


if __name__ == '__main__':
    start_web_app()
