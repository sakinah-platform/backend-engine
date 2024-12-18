import random
import string

def string_for_date() -> str:

    return '%Y-%m-%d'

def string_for_datetime(separator: str = ';') -> str:

    return string_for_date() + separator + '%H:%M'

DATE_FORMATS = [ string_for_date() ]
DATETIME_FORMATS = [ string_for_datetime(';') ]

DEFAULT_CACHE_TIME = 60 * 10