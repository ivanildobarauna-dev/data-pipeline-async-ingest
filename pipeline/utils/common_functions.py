from datetime import datetime


def default_timestamp_str() -> str:
    return str(int(datetime.now().timestamp()))


def default_timestamp_formated() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
