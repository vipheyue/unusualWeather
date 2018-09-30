from app.notice.mail import send_email

if __name__ == '__main__':
    send_email.delay("vipheyue@foxmail.com","task_launcher222")
    print(send_email.name)