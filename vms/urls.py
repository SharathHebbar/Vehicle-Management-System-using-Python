from django.urls import path
from . import views
urlpatterns = [
    path('', views.welcome),
    path('login', views.login),
    path('signup', views.signup),

    path('index', views.index),

    path('vehicle', views.vehicle),
    path('driver', views.driver),
    path('fuel', views.fuel),
    path('booked', views.booked),
    path('vehicle_history', views.vehicle_history),

    path('report', views.report),
    path('full_report', views.full_report),


    path('Contactus', views.contact),
    path('logout', views.logout),


]
