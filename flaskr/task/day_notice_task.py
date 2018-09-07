import schedule
import time
from flaskr.notice.mail import send_email
from flaskr.weather.caiyun import check_unuaual_weather, realtime


def job():
    # 121.6544,25.1552

    # longitude = 116.298056  # 经度-何悦
    # latitude = 39.959912  # 纬度
    longitude = 121.6544  # 经度
    latitude = 25.1552  # 纬度
    # realtime(longitude, latitude)
    result = check_unuaual_weather(longitude, latitude)
    if result != '':
        # 发送邮件
        send_email("vipheyue@foxmail.com", result)
        return result


def schedule_task():
    # schedule.every(2).seconds.do(job)
    schedule.every().day.at("9:00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(20)


import logging
from flaskr.log.log_manager import initLog
from flaskr.log.test import testlog

logger = logging.getLogger('main.task')
if __name__ == '__main__':

    # initLog()
    # logger.info("xcxcxc")
    # testlog()

    schedule_task()

