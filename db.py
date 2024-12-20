from pymongo import MongoClient

from secrets import Secrets


def get_database():
    connection_str = Secrets.db_url
    client = MongoClient(connection_str)
    return client['jobs']


def insert_jobs(collection, job_listings):
    for job in job_listings:
        job_id = job['id']
        collection.update_one(
            {'id': job_id},
            {'$setOnInsert': job},
            upsert=True
        )