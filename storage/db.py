from pymongo import MongoClient

from constants.secrets import Secrets


def get_database():
    connection_str = Secrets.db_url
    client = MongoClient(connection_str)
    return client['jobs']


def insert_jobs(collection, job_listings) -> list:
    job_notification = []
    for job in job_listings:
        job_id = job['id']
        result = collection.update_one(
            {'id': job_id},
            {'$setOnInsert': job},
            upsert=True
        )
        if result.upserted_id:
            job_notification.append(job)
    return job_notification