# encoding:utf-8
from pprint import pprint
import time

from flask import Flask, request, url_for
import config

from app.notice.mail import send_email
from app.weather.caiyun import realtime, daily_forest
from app.user.user import user_blueprints

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(user_blueprints, url_prefix='/user')


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    print(" net hello world")
    return 'Hello, World!!!!+++ %s' % time.asctime()


@app.route('/unusualWeather', methods=['GET', 'POST'])
def unusual_weather():
    if request.method == 'POST':
        longitude = request.form['longitude']
        latitude = request.form['latitude']
        receiverEmail = request.form['receiverEmail']
        result = daily_forest(longitude, latitude)
        if result != '':
            # 发送邮件
            send_email(receiverEmail, result)
            return str(result)
        return "no unusual weather."
    else:
        return 'get method  no support'


@app.route('/sendMail', methods=['GET', 'POST'])
def send_mail():
    result = send_email("vipheyue@foxmail.com", "邮件测试")
    return str(result)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/scheduler/start')
def scheduler_start():
    from app.task.task_manager import g_scheduler
    g_scheduler.start()
    return 'g_scheduler.start()'


@app.route('/scheduler/startJob')
def scheduler_startJob():
    from app.task.task_manager import g_scheduler
    from app.task.task_manager import add_job
    add_job()
    scheduler_start()
    return get_jobs()


@app.route('/scheduler/get_jobs')
def get_jobs():
    from app.task.task_manager import get_jobs
    return get_jobs()


@app.route('/scheduler/shutdown')
def test3():
    from app.task.task_manager import g_scheduler
    g_scheduler.shutdown()
    return 'shutdown'


def application(env, start_response):
    str(env)
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"Hello World------------------"]


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # hello_world()
    # schedule_task()
