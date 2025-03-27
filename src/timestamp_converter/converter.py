from datetime import datetime
from typing import Union


def unix_to_timestamp(unixtimestamp: Union[int, float]) -> str:
    """
    Convert a Unix timestamp to an ISO formatted timestamp.

    Parameters:
        unixtimestamp (int or float): Unix timestamp.

    Returns:
        str: ISO formatted timestamp.
    """
    return datetime.fromtimestamp(unixtimestamp).isoformat()
