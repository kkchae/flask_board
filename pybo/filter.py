import datetime

def format_datetime(value : datetime, format='%Y-%m-%d %H:%M:%S'):
    return value.strftime(format)