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


def is_unixtimestamp(unixtimestamp):
    """
    Check if the given integer is a valid Unix timestamp.

    Parameters:
        unixtimestamp (int): Unix timestamp to check.

    Returns:
        bool: True if valid Unix timestamp, False otherwise.
    """
    if not isinstance(unixtimestamp, int):
        return False
    try:
        datetime.fromtimestamp(unixtimestamp)
        return True
    except (OverflowError, OSError, ValueError):
        return False


if __name__ == '__main__':
    print(unix_to_timestamp(1731394800))  # 2024-11-12T11:00:00
