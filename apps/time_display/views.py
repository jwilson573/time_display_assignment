from django.shortcuts import render, redirect
from datetime import datetime
import pytz
from pytz import timezone


def index(request):
    current = pytz.utc.localize(datetime.now())
    central = timezone('America/Chicago')
    time = {
        'dateTime': current.astimezone(central).strftime("%b %d, %Y %I:%M %p"),
    }

    return render(request, "time_display/index.html",time)
