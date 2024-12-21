from datetime import datetime
import pytz

from constants.const import date_format, us_pacific, chat_time, human_date, us_date, human_date_lower


def date_convert_dmy(date_str: str):
    input_date = datetime.strptime(date_str, us_date)
    return input_date.strftime(date_format)

def date_convert_str(date_str: str):
    input_date = datetime.strptime(date_str, human_date_lower)
    return input_date.strftime(date_format)

def date_convert_iso(date_str: str):
    input_date = datetime.fromisoformat(date_str)
    return input_date.strftime(human_date)

def get_pst():
    utc_now = datetime.now(pytz.utc)
    pst_timezone = pytz.timezone(us_pacific)
    pst_now = utc_now.astimezone(pst_timezone)
    return pst_now.strftime(chat_time)