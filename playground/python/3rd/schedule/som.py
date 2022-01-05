from datetime import datetime, timedelta

# from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio


# Start the scheduler
sched = AsyncIOScheduler()

# Define the function that is to be executed
def my_job(text):
    print(text)


# The job will be executed on November 6th, 2009
exec_date = datetime.now() + timedelta(seconds=10)

# Store the job in a variable in case we want to cancel it
job = sched.add_job(my_job, "date", run_date=exec_date, args=["text"])

sched.start()
asyncio.get_event_loop().run_forever()
