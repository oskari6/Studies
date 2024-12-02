import schedule
import time
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

def task():
    print("task executed")

schedule.every(10).seconds.do(task)
schedule.every().minute.do(task)
schedule.every().hour.do(task)
schedule.every().day.at("10:00").do(task)
job = schedule.every().friday.at("15:00").do(task)
schedule.cancel_job(job)

while True:
    schedule.run_pending()
    time.sleep(1)

#apscheduler
scheduler = BackgroundScheduler()

def task_with_args(name):
    print(name)

scheduler.add_job(task, "interval", seconds=10)
scheduler.add_job(task, "cron", hour=10, minute=30)
scheduler.ad_job(task, "date", run_date=datetime(2024, 12, 25, 6 ,30))
scheduler.ad_job(task_with_args, "interval", seconds=5, args=["hello"])

scheduler.start()

try:
    while True:
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()

job_stores = {
    "default": SQLAlchemyJobStore(url="sqlite://jobs.sqlite")
}

scheduler.start()
