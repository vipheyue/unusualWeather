from app.notice.mail import send_email
from app.task.daily.daily_task import interval_rain_monitor
if __name__ == '__main__':
    # send_email.delay("vipheyue@foxmail.com","task_launcher222")
    # print(send_email.name)
    interval_rain_monitor.delay()
