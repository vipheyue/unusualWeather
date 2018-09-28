from app.celery_module.celeryapp import add



if __name__ == '__main__':
    result=add.delay(6, 74)
    print(result)
    print(result.ready())
