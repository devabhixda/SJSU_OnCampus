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
    print(f'Fetched {len(flattened_jobs)} jobs')
    job_notifications = insert_jobs(collection, flattened_jobs)
    print(f'Found {len(job_notifications)} new jobs')
    asyncio.run(send_notification(job_notifications))

if __name__ == "__main__":
    get_jobs()