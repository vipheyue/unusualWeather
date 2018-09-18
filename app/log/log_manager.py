import logging
from logging.handlers import HTTPHandler
import sys


def initLog():
    logger = logging.getLogger('main')
    logger.setLevel(level=logging.DEBUG)
    # StreamHandler
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(level=logging.DEBUG)
    logger.addHandler(stream_handler)

    # FileHandler
    file_handler = logging.FileHandler('main.log')
    file_handler.setLevel(level=logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # HTTPHandler
    # http_handler = HTTPHandler(host='localhost:8001', url='log', method='POST')
    # logger.addHandler(http_handler)

initLog()

if __name__ == '__main__':
    logger = logging.getLogger('main')
    logger.info('This is a log info')
    logger.debug('Debugging')
    logger.warning('Warning exists...')
    logger.info('Finish')
