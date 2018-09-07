# coding=utf-8
import smtplib
from email.mime.text import MIMEText


def send_email(receiver, content):
    msg_from = 'vipheyue@foxmail.com'  # 发送方邮箱
    passwd = 'tqaquuorzxxdbjdf'  # 填入发送方邮箱的授权码

    subject = "异常天气提醒"  # 主题
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = receiver
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号
        s.login(msg_from, passwd)
        s.sendmail(msg_from, receiver, msg.as_string())
        print("发送成功")
    except s.SMTPException:
        print("发送失败" + receiver + content)
    finally:
        s.quit()


if __name__ == '__main__':
    content = "这是我使用python smtplib及email模块发送的邮件"  # 正文
    send_email("vipheyue@foxmail.com", content)
