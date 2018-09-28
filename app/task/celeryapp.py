from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

# 默认的pip celery有问题
# pip install --upgrade https://github.com/celery/celery/tarball/master
app = Celery('celeryapp')

app.config_from_object('app.task.celeryconfig')
# 可见性超时
app.conf.broker_transport_options = {'visibility_timeout': 60}

# app.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'app.task.tasks.add',
#         'schedule': 2.0,
#         'args': (16, 16)
#     },
# }


from celery.schedules import crontab


# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     print("-----")
#     sender.add_periodic_task(2.0, test.s('hello'), name='add every 10')
#
#     # Calls test('world') every 30 seconds
#     sender.add_periodic_task(4.0, test.s('world'), expires=10)
#
#     # Executes every Monday morning at 7:30 a.m.
#     sender.add_periodic_task(
#         crontab(hour=7, minute=30, day_of_week=1),
#         test.s('Happy Mondays!'),
#     )


@app.task
def test(arg):
    print(arg)

# if __name__ == '__main__':
# app.start()
