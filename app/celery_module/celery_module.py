from celery import Celery

celery_app = Celery()
celery_app.timezone = 'Asia/Shanghai'
print(celery_app.timezone)
