import os


def start_daily_task():
    os.system("nohup python ../app/task/day_notice_task.py &")
if __name__ == '__main__':
    start_daily_task()