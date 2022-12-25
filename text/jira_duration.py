#!/usr/bin/env python3

"""
copy a jira page containing the "Original estimate" column to clipboard.
Then:
clip -o | ./jira_duration.py
"""

import sys
from datetime import timedelta

units = {
    'week': timedelta(days=5),
    'day': timedelta(days=1),
    'hour': timedelta(hours=1),
}
duration = timedelta(0)
for line in sys.stdin:
    for unit in units:
        if unit in line:
            quantity = int(line.split(unit)[0].rsplit()[-1])
            duration += quantity * units[unit]
            break
print(duration)
