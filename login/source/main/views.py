from django.views.generic import TemplateView, CreateView, ListView
from carpool.models import User
from collections import namedtuple
import json
from django.shortcuts import render

class IndexPageView(TemplateView):
    template_name = 'main/index.html'

class ChangeContactView(TemplateView):
    template_name = 'main/contact.html'

class ChangeAboutView(TemplateView):
    template_name = 'main/about.html'

def RideView(request):
    data = User.objects.all()
    if not data.exists():
        return render(request, "main/ride.html")
    Driver = namedtuple('Driver', 'mpg capacity destination source time')
    Passenger = namedtuple('Passenger', 'destination source time')
    drivers = []
    passengers = []
    for u in data.iterator():
        if u.mpg and u.capacity and u.destination and u.source and u.departure_time:
            drivers.append(Driver(u.mpg, u.capacity, u.destination, u.source, u.departure_time))
        elif u.destination and u.source and u.departure_time:
            passengers.append(Passenger(u.destination, u.source, u.departure_time))
    return render(request, "main/ride.html", {
        # "drivers": User.objects.all(),
        "driver": drivers,
        "passenger": passengers
    })
    # api_key = 'AIzaSyDDgkyK4kheG5dXqh1pSniauXiZJ7ahwDw'
    # url = "https://maps.googleapis.com/maps/api/distancematrix/json?"
    # r = requests.get(url + 'origins = dehradun&destinations = haridwar&key=' + api_key)
    # x = r.json()
    # print(x)
