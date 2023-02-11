import django_tables2 as tables
from django.utils.html import format_html
from django.urls import reverse
from .models import Bus, Route, BusRoute


class BusModelTable(tables.Table):
    Number_of_routes = tables.Column(accessor='totalbus', verbose_name='Number of routes this bus runs on')

    class Meta:
        model = Bus
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id', 'bus_name', 'bus_number', 'Number_of_routes')

    def render_Number_of_routes(self, value, record):
        url = reverse('busroutes', args=[record.bus_number])
        return format_html('<a href="{}">{}</a>', url, value)


class BusRoutesModelTable(tables.Table):
    route_number = tables.Column(accessor='route.route_number')

    class Meta:
        model = BusRoute
        template_name = "django_tables2/bootstrap4.html"
        fields = ('route', 'route_number', 'from_time', 'to_time')


class RouteModelTable(tables.Table):
    Number_of_buses = tables.Column(accessor='totalbus', verbose_name='Number of buses running on this route')

    class Meta:
        model = Route
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id', 'route_name', 'route_number', 'Number_of_buses')

    def render_Number_of_buses(self, value, record):
        url = reverse('routebusestable', args=[record.route_number])
        return format_html('<a href="{}">{}</a>', url, value)

    
class RouteBusesModelTable(tables.Table):
    bus_number = tables.Column(accessor='bus.bus_number')

    class Meta:
        model = BusRoute
        template_name = "django_tables2/bootstrap4.html"
        fields = ('bus', 'bus_number', 'from_time', 'to_time')
