from flask import Blueprint, request

scheduler_blueprints = Blueprint('scheduler', __name__)


@scheduler_blueprints.route('/start')
def scheduler_start():
    from app.task.task_manager import g_scheduler
    g_scheduler.start()
    return 'g_scheduler.start()'


@scheduler_blueprints.route('/startJob')
def scheduler_startJob():
    from app.task.task_manager import g_scheduler
    from app.task.task_manager import add_job
    add_job()
    scheduler_start()
    return get_jobs()


@scheduler_blueprints.route('/getJobs')
def get_jobs():
    from app.task.task_manager import get_jobs
    return get_jobs()


@scheduler_blueprints.route('/removeJobById', methods=['GET', 'POST'])
def remove_job_by_id():
    from app.task.task_manager import remove_job
    jobId = request.form['jobId']
    remove_job(jobId)
    return "done"


fadetop_id = ""


@scheduler_blueprints.route('/fadetopStart')
def fadetop_start():
    from app.task.task_manager import g_scheduler
    import uuid
    global fadetop_id
    fadetop_id = str(uuid.uuid1())
    # g_scheduler.add_job(fade_top, 'cron', hour='7-20/1', id=fadetop_id)
    g_scheduler.add_job(fade_top, 'interval', minutes=35, id=fadetop_id)
    # g_scheduler.add_job(fade_top, 'interval', seconds=5, id=fadetop_id)
    # g_scheduler.add_job(fade_top, 'cron', hour=13, minute=37, id=str(uuid.uuid1()))

    if not g_scheduler.running:
        g_scheduler.start()
    return 'fadetopStart'


@scheduler_blueprints.route('/fadetopShutdown')
def fadetop_shutdown():
    from app.task.task_manager import g_scheduler
    from app.task.task_manager import remove_job
    remove_job(fadetop_id)
    return 'fadetopShutdown'


def fade_top():
    from app.notice.mail import send_email
    send_email("vipheyue@foxmail.com", "起来一下")


@scheduler_blueprints.route('/shutdown')
def shutdown():
    from app.task.task_manager import g_scheduler
    g_scheduler.shutdown()
    return 'shutdown'
