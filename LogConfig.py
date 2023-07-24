import logging


def setup_logging():

    logger = logging.getLogger('mylogger')
    if logger.handlers:
        return logger
    logger.setLevel(logging.DEBUG)

    file_hander = logging.FileHandler('log.txt', 'w')
    file_hander.setLevel(logging.DEBUG)

    stream_hander = logging.StreamHandler()
    stream_hander.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_hander.setFormatter(formatter)
    stream_hander.setFormatter(formatter)

    logger.addHandler(file_hander)
    logger.addHandler(stream_hander)
    return logger
