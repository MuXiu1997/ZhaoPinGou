import datetime
import os

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from setting import XLSX_PATH


def job():
    last_day = (datetime.datetime.now() - datetime.timedelta(days=1)).timestamp()
    for filename in os.listdir(XLSX_PATH):
        if os.path.splitext(filename)[1] == '.xlsx':
            file_path = os.path.join(XLSX_PATH, filename)
            stats = os.stat(file_path)
            if last_day > stats.st_mtime:
                os.remove(file_path)


def scheduler():
    trigger = CronTrigger(day='*')
    _scheduler = BackgroundScheduler(timezone="Asia/Shanghai")
    _scheduler.add_job(job, trigger=trigger)
    return _scheduler


if __name__ == '__main__':
    job()
