import datetime
from rest_framework.response import Response

def deny_after_10pm(func):
    def wrapper(request, *args, **kwargs):
        current_hour = datetime.datetime.now().hour
        if current_hour > 22:
            return Response({"error": "Access not allowed after 10 PM"}, status=403)
        return func(request, *args, **kwargs)
    return wrapper

# 👇 New Decorator: Allow only on weekdays
def allow_only_weekdays(func):
    def wrapper(request, *args, **kwargs):
        today = datetime.datetime.now().weekday()  # Monday = 0, Sunday = 6
        if today in [5, 6]:  # Saturday or Sunday
            return Response({"error": "Access not allowed on weekends"}, status=403)
        return func(request, *args, **kwargs)
    return wrapper