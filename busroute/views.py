from django.shortcuts import render
from busroute.models import Bus, Route, BusRoute
from busroute.tables import BusModelTable, RouteModelTable, BusRoutesModelTable, RouteBusesModelTable


def index(request):
    if request.method == 'GET':
        return render(request, "index.html")


def bustables(request):
    if request.method == 'GET':
        table = BusModelTable(Bus.objects.all())
        return render(request, 'table.html', {'table': table})


def busroutestable(request, id):
    if request.method == 'GET':
        buss = Bus.objects.get(bus_number=id)
        table = BusRoutesModelTable(BusRoute.objects.filter(bus=buss))
        return render(request, 'table.html', {'table': table})
        

def routetables(request):
    if request.method == 'GET':
        table = RouteModelTable(Route.objects.all())
        return render(request, 'table.html', {'table': table})


def routebusestable(request, id):
    if request.method == 'GET':
        routess = Route.objects.get(bus=id)
        table = RouteBusesModelTable(BusRoute.objects.filter(route=routess))
        return render(request, 'table.html', {'table': table})

