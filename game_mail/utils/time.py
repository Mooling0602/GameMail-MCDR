from ..import_api import *

def get_timestamp() -> str:
    timestamp = datetime.now(pytz.timezone("Asia/Shanghai")).strftime('%Y-%m-%dT%H:%M:%S%z')
    return timestamp