from datetime import datetime, timedelta

today = datetime.now()
five_days_ago = today - timedelta(days=5)

print("5 days ago:", five_days_ago)

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


without_microseconds = today.replace(microsecond=0)

print("Without microseconds:", without_microseconds)


date1 = datetime(2026, 9, 25)
date2 = datetime(2026, 9, 30)

difference = date2 - date1
seconds = difference.total_seconds()

print("Difference in seconds:", seconds)