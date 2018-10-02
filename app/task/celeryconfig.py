
from celery.schedules import crontab

# broker_url = 'redis://s.welightworld.com:6379/0'
# result_backend = 'redis://s.welightworld.com:6379/1'
broker_url = 'redis://localhost:6379/0'
result_backend = 'redis://localhost:6379/1'

# task_serializer = 'json'
# result_serializer = 'json'
# accept_content = ['json']
timezone = 'Asia/Shanghai'
enable_utc = True
imports = ("app.task.tasks",'app.notice.mail')
beat_schedule = {
    'taskA_schedule': {
        'task': 'app.task.tasks.add',
        'schedule': crontab(hour=7, minute=20),
        'args': (5, 6)
    },

    'app.task.weather_task.dailyWeatherA': {
        'task': 'app.task.weather_task.dailyWeather',
        'schedule': crontab(hour=7, minute=20),
        'args': ()
    },
    'app.task.weather_task.dailyWeatherB': {
        'task': 'app.task.weather_task.dailyWeather',
        'schedule': crontab(hour=18, minute=00),
        'args': ()
    },
    'app.task.weather_task.dailyWeatherTEST': {
        'task': 'app.task.daily.daily_task.interval_rain_monitor',
        'schedule': crontab(hour=13),
        'args': ()
    }

}
