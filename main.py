from itertools import chain

from db import get_database, insert_jobs
from scrapper import scrap_sources


def get_jobs():
    jobs = scrap_sources()
    db = get_database()
    collection = db['daily_dump']
    flattened_jobs = list(chain(*jobs))
    insert_jobs(collection, flattened_jobs)

if __name__ == "__main__":
    get_jobs()