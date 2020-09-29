import json
from typing import Dict


def is_valid_json(object_to_check: Dict):
    try:
        json.dumps(object_to_check)
        return True
    except TypeError as err:
        return False
