import datetime
import time


def create_timestamp_querystring():
    timestamp = int(time.time() * 1000)
    return dict(timestamp=timestamp)


def get_date_str():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    return '{}-{}-{}'.format(year, month, day)
