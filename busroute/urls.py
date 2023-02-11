from django.urls import path
from busroute.views import index, bustables, routetables, busroutestable, routebusestable

urlpatterns = [
    path('', index, name="index"),
    path('buses/', bustables, name="buses"),
    path('routes/', routetables, name="routes"),
    path('busroutestable/<int:id>', busroutestable, name="busroutes"),
    path('routebusestable/<int:id>', routebusestable, name="routebusestable"),

]