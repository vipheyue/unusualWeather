from __future__ import absolute_import

import uuid

from app.notice.mail import send_email
from app.weather.caiyun import daily_forest, have_rain_detail, rain_2h, forecast_data, \
    rain_monitor
from pytz import utc

from app.task.celeryapp import app


@app.task(autoretry_for=(Exception,), default_retry_delay=60 * 3, retry_kwargs={'max_retries': 5})
def dailyWeather():
    longitude = 116.298056  # 经度-何悦
    latitude = 39.959912  # 纬度
    result = daily_forest(longitude, latitude)
    send_email("vipheyue@foxmail.com", result)




if __name__ == '__main__':
    print(dailyWeather)
    print(dailyWeather.name)
    # dailyWeather.delay()
