import logging
logger = logging.getLogger('main.test')
def testlog():
    logger.info(".........")

if __name__ == '__main__':
    from app.log.log_manager import get_log
    get_log().info(".....")
