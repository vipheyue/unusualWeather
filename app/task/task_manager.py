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
    __first_init = True
    def __init__(self):
        if self.__first_init:
            self.g_scheduler = BackgroundScheduler(timezone=pytz.timezone('Asia/Shanghai'))
            self.__class__.__first_init = False
    # g_scheduler = BlockingScheduler(timezone=pytz.timezone('Asia/Shanghai'))


# tm = TaskManager()
# g_scheduler = tm.g_scheduler
from app.run import g_scheduler



def job1():
    print("执行任务时间: %s" % time.asctime())





def add_job():
    print(uuid.uuid1())
    # g_scheduler.add_job(job1, 'date', run_date=datetime(2018, 9, 16, 12, 30, 10), args=[])
    # g_scheduler.add_job(job1, 'interval', seconds=2)
    # g_scheduler.add_job(interval_rain_monitor, 'interval', seconds=10)
    # g_scheduler.add_job(dailyWeather, 'cron', hour=13, minute=14)
    # g_scheduler.add_job(dailyWeather, 'cron', hour=7, minute=20, id=str(uuid.uuid1()))
    # g_scheduler.add_job(dailyWeather, 'cron', hour=18, minute=0, id=str(uuid.uuid1()))

    # g_scheduler.add_job(rain_post, 'cron', hour=7, minute=26)
    # g_scheduler.add_job(rain_post, 'cron', hour=18, minute=1)
    # g_scheduler.add_job(interval_rain_monitor, 'cron', hour='7-20/2', id=str(uuid.uuid1()))
    # g_scheduler.add_job(interval_rain_monitor, 'cron', minute='7-59/1')

    # g_scheduler.add_job(job1, 'cron', hour=17, minute=1)

    g_scheduler.print_jobs()




if __name__ == '__main__':
    add_job()
    g_scheduler.start()
    # get_jobs()
    # dailyWeather()
    # job1()

    from app.log.log_manager import get_log

    get_log().info(".....")
