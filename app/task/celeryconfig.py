import flower
from celery.schedules import crontab
broker_url = 'redis://s.welightworld.com:6379/0'
result_backend = 'redis://s.welightworld.com:6379/1'
# broker_url = 'redis://localhost:6379/0'
# result_backend = 'redis://localhost:6379/1'

# task_serializer = 'json'
# result_serializer = 'json'
# accept_content = ['json']
timezone = 'Asia/Shanghai'
enable_utc = True
imports = ("app.task.tasks", 'app.notice.mail', 'app.task.weather_task')
beat_schedule = {
    'taskA_schedule': {
        'task': 'app.task.tasks.add',
        'schedule': crontab(hour=7, minute=20),
        'args': (5, 6)
    },

    'app.task.weather_task.dailyWeatherA': {
        'task': 'app.task.weather_task.dailyWeather',
        'schedule': crontab(hour=0, minute=1),
        'args': ()
    },
    # 'app.task.weather_task.dailyWeatherTEST': {
    #     'task': 'app.task.weather_task.dailyWeather',
    #     'schedule': crontab(hour=12, minute=35),
    #     'args': ()
    # },
    'app.task.weather_task.interval_rain_monitor': {
        'task': 'app.task.weather_task.interval_rain_monitor',
        'schedule': crontab(hour='7-19/1'),
        'args': ()
    },
    'app.task.weather_task.interval_rain_monitor_TEST': {
        'task': 'app.task.weather_task.interval_rain_monitor',
        'schedule': crontab(minute='*/1'),
        'args': ()
    },

}




