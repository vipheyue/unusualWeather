import uuid
from datetime import datetime

import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
import time
from app.notice.mail import send_email
from app.weather.caiyun import daily_forest, have_rain_detail, rain_2h, forecast_data, \
    rain_monitor
from pytz import utc
from app.base.singleton import SingletonMetaclass


class TaskManager(metaclass=SingletonMetaclass):
    g_scheduler = BackgroundScheduler(timezone=pytz.timezone('Asia/Shanghai'))
    print("---------g_scheduler--------")
    print(str(g_scheduler))

    # g_scheduler = BlockingScheduler(timezone=pytz.timezone('Asia/Shanghai'))
    def job1(self):
        print("执行任务时间: %s" % time.asctime())

    def dailyWeather(self):
        longitude = 116.298056  # 经度-何悦
        latitude = 39.959912  # 纬度
        result = daily_forest(longitude, latitude)
        send_email("vipheyue@foxmail.com", result)

    def interval_rain_monitor(self):
        longitude = 116.298056  # 经度-何悦
        latitude = 39.959912  # 纬度
        result = rain_monitor(longitude, latitude)
        if result != '':
            send_email("vipheyue@foxmail.com", result)  # 发送邮件

    def add_job(self):
        global g_scheduler
        print(uuid.uuid1())
        # g_scheduler.add_job(job1, 'date', run_date=datetime(2018, 9, 16, 12, 30, 10), args=[])
        # g_scheduler.add_job(job1, 'interval', seconds=2)
        # g_scheduler.add_job(interval_rain_monitor, 'interval', seconds=10)
        # g_scheduler.add_job(dailyWeather, 'cron', hour=13, minute=14)
        g_scheduler.add_job(dailyWeather, 'cron', hour=7, minute=20, id=str(uuid.uuid1()))
        g_scheduler.add_job(dailyWeather, 'cron', hour=18, minute=0, id=str(uuid.uuid1()))

        # g_scheduler.add_job(rain_post, 'cron', hour=7, minute=26)
        # g_scheduler.add_job(rain_post, 'cron', hour=18, minute=1)
        g_scheduler.add_job(interval_rain_monitor, 'cron', hour='7-20/2', id=str(uuid.uuid1()))
        # g_scheduler.add_job(interval_rain_monitor, 'cron', minute='7-59/1')

        # g_scheduler.add_job(job1, 'cron', hour=17, minute=1)

        g_scheduler.print_jobs()

    def get_jobs(self):
        print(str(g_scheduler))
        jobs = g_scheduler.get_jobs()
        result = ""
        for job in jobs:
            result += str(job) + " id : " + job.id + "\n"
        print(result)
        return result

    def remove_job(self,job_id):
        g_scheduler.remove_job(job_id)


if __name__ == '__main__':
    add_job()
    g_scheduler.start()
    # get_jobs()
    # dailyWeather()
    # job1()

    from app.log.log_manager import get_log

    get_log().info(".....")
