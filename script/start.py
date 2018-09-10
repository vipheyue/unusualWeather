#!/bin/python3
import os

import time


def start_web_app():
    os.system("echo start_web_app---")
    os.system("cd /opt/unusualWeather/")
    os.system("git fetch —a ")
    os.system("git fetch origin master")
    os.system("git reset --hard origin/master ")
    os.system("echo ---end---")

    # os.system(". venv/bin/activate")
    # os.system("uwsgi uwsgi.ini")
    # time.sleep(1)


if __name__ == '__main__':
    start_web_app()
