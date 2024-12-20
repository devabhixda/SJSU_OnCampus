import os

class Secrets:
    db_url = os.environ.get('DB_URL')