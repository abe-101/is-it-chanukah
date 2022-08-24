import datetime
from zmanim.hebrew_calendar.jewish_date import JewishDate
from zmanim.hebrew_calendar.jewish_calendar import JewishCalendar

from django.shortcuts import render

# Create your views here.

def index(request):
    date = JewishDate()
    today = JewishCalendar(date.jewish_year, date.jewish_month, date.jewish_day)
    
    return render(request, "isitchanukah/index.html", {
        "chanukah": today.is_chanukah()
        })
