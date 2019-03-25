from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import *

def home(request):
    date = dt.date.today()
    return render(request, 'home.html', {"date": date})


def neighborhood(request):
    date = dt.date.today()
    return render(request, 'neighborhood.html', {"date": date})

def convert_dates(dates):

    
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    day = days[day_number]
    return day
