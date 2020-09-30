import json
from typing import Dict


def is_valid_json(object_to_check: Dict):
    try:
        json.dumps(object_to_check)
        return True
    except TypeError as err:
        return False


def sql_object_to_dict(sql_object):
    data = {}
    for column in sql_object.__table__.columns:
        data[column.name] = str(getattr(sql_object, column.name))

    return data
