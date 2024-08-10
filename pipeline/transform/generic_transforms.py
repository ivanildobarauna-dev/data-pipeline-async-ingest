import json
from datetime import datetime


def set_key(element, key_name: str, extract_num_chars: int):
    data = json.loads(element)
    key = data.get(key_name, "")
    return str(key)[:extract_num_chars], element


def set_datetime(element, datetime_field_name: str, data_field_name: str):
    return [
        {datetime_field_name: datetime.now(), data_field_name: item} for item in element
    ]
