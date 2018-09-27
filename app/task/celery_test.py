from app.celery_module.celery_module import celery_app as app


@app.task
def add(x, y):
    return x + y


if __name__ == '__main__':
    print(add.name)
    print(app.tasks['__main__.add'])
