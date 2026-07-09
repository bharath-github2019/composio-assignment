"""
Composio Research Agent - Utilities
Caching, logging, timestamp helpers.
"""
import time
import json
from datetime import datetime, timezone

def timestamp() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

def log_error(error_log: list, app: str, field: str, message: str):
    error_log.append({
        "app_name": app,
        "field": field,
        "message": message,
        "timestamp": timestamp()
    })

class Timer:
    def __init__(self):
        self.start = time.time()
    def elapsed(self) -> int:
        return int(time.time() - self.start)
