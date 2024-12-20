from datetime import datetime

from const import date_format


def date_convert_dmy(date_str: str):
    input_date = datetime.strptime(date_str, "%m/%d/%Y")
    return input_date.strftime(date_format)

def date_convert_str(date_str: str):
    input_date = datetime.strptime(date_str, "%b %d, %Y")
    return input_date.strftime(date_format)

def date_convert_iso(date_str: str):
    input_date = datetime.fromisoformat(date_str)
    return input_date.strftime("%B %d, %Y")