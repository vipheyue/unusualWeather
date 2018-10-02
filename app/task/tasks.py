from app.task.celeryapp import app, test


@app.task
def print_task(x):
    print("--:       " + x)


@app.task(autoretry_for=(Exception,), default_retry_delay=5, retry_kwargs={'max_retries': 5})
def add(x, y):
    print("------------" + "x=" + str(x) + "  y=" + str(y))
    from app.notice.mail import send_email
    # result = send_email("vipheyue@foxmail.com", "邮件测试 " + "x=" + str(x) + "  y=" + str(y))
    return x + y


if __name__ == '__main__':
    from app.notice.mail import send_email

    result = send_email.delay("vipheyue@foxmail.com", "邮件测试 " + "x=" + str(1) + "  y=" + str(2))
    # task_send_mail.delay("邮件测试-----2")
    # result = add.apply_async((2, 2), link=add.s(16))
    # print(result)

    # print_task.delay("xxx")
    # test.delay("xxx")
    # print(task_send_mail.name)
    # print(interval_rain_monitor.delay())
    # print(interval_rain_monitor.name)
    # print(print_task.name)
    # print(type(print_task))
    # result = add.delay(6, 4)
    # print(result)
    # print(result.ready())
    # print(result.get(timeout=1))
    # print(result.state)
    # s1=add.signature((2, 3), countdown=100)
    # s1 = add.s(2, 2)
    # res = s1.delay()
    # print(res.get())
    # s2 = add.s(2)
    # res = s2.delay(8)
    # res.get()
    # add.apply_async((2, 0), queue='hipri',debug=True)
