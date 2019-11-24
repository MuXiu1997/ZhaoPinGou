import logging
import os
import time
import traceback

logger = logging.getLogger()
logger.setLevel(logging.INFO)

date = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
log_path = os.path.join(os.getcwd(), 'logs')
if not os.path.exists(log_path):
    os.mkdir(log_path)
log_name = '{}.log'.format(date)
log_file = os.path.join(log_path, log_name)

formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def error_handler(e):
    _ = e
    logger.error(traceback.format_exc())
