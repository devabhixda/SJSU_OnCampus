import os

class Secrets:
    chat_id = os.environ.get('CHAT_ID')
    db_url = os.environ.get('DB_URL')
    tg_token = os.environ.get('TG_TOKEN')