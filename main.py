import asyncio
from itertools import chain

from storage.db import get_database, insert_jobs
from notification.telegram import send_notification
from utils.scrapper import scrap_sources


def get_jobs():
    jobs = scrap_sources()
    db = get_database()
    collection = db['daily_dump']
    flattened_jobs = list(chain(*jobs))
    job_notifications = insert_jobs(collection, flattened_jobs)
    if job_notifications:
        asyncio.run(send_notification(job_notifications))
    else:
        print('No new jobs found')

if __name__ == "__main__":
    get_jobs()