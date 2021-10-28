import logging

def logger_fn():
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter('%(filename)s ,%(name)s,  %(levelname)s , %(message)s')
    file_handler = logging.FileHandler('errorlog.log')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)

    logger.info('issue detected')
    return logger


# print('logger name: ',__name__)


