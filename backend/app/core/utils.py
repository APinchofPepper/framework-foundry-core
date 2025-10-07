from datetime import datetime

import pytz


def format_datetime(
    dt: datetime, fmt: str = "%Y-%m-%d %H:%M:%S", timezone: str = "US/Pacific"
) -> str:
    """Format datetime in the specified timezone"""
    if dt.tzinfo is None:
        # If datetime is naive (no timezone), assume it's UTC
        dt = pytz.UTC.localize(dt)

    # Convert to the specified timezone
    local_tz = pytz.timezone(timezone)
    local_dt = dt.astimezone(local_tz)

    return local_dt.strftime(fmt)


def validate_email(email: str) -> bool:
    import re

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None
