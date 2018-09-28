from celery import Celery
#默认的pip celery有问题
# pip install --upgrade https://github.com/celery/celery/tarball/master
app = Celery('celeryapp',backend='redis://localhost:6379/1', broker='redis://localhost:6379/0')


class Config:
    enable_utc = True
    timezone = 'Asia/Shanghai'


app.config_from_object(Config)
# app.conf.broker_url = 'redis://localhost:6379/0'
# 可见性超时
app.conf.broker_transport_options = {'visibility_timeout': 60}
# 在Redis中存储状态并返回任务值
# app.conf.result_backend = 'redis://localhost:6379/0'



@app.task
def add(x, y):
    print("i am add  fun ")
    from app.notice.mail import send_email
    # result = send_email("vipheyue@foxmail.com", "邮件测试4 " + str(y))
    return x + y

if __name__ == '__main__':
    app.start()