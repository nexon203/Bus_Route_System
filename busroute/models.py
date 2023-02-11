from django.db import models


class Route(models.Model):
    route_name = models.CharField(max_length=50, null=False, blank=False)
    route_number = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def totalbus(self):
        N = BusRoute.objects.filter(route=self.id).count()
        return N

    def __str__(self):
        return self.route_name


class Bus(models.Model):
    bus_name = models.CharField(max_length=50, null=False, blank=False)
    bus_number = models.IntegerField(null=False, blank=False)
    bus_route = models.ManyToManyField(Route, through='BusRoute')
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def totalbus(self):
        N = self.bus_route.count()
        return N

    def __str__(self):
        return self.bus_name


class BusRoute(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    from_time = models.DateTimeField()
    to_time = models.DateTimeField()

    def __str__(self):
        return (f"Bus:{self.bus} in route:{self.route}")
