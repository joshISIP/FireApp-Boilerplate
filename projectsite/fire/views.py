from django.shortcuts import render
from django.views.generic.list import ListView
from fire.models import Locations, Incident, FireStation


class HomePageView(ListView):
    model = Locations
    context_object_name = 'home'
    template_name = "home.html"


def map_station(request):
    fire_station = FireStation.objects.values('name', 'latitude', 'longitude')

    for fs in fire_stations:
        fs['latitude'] = float(fs['latitude'])
        fs['longitude'] = float(fs['longitude'])

    context = {
        'fire_station': fire_station_list,  
    }
    return render(request, 'map_station.html', context)
