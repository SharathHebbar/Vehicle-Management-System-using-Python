from django.shortcuts import redirect, render
from .models import *
# Create your views here.


def welcome(request):
    return render(request, 'vms/welcome.html')


def login(request):
    return render(request, 'vms/login.html')


def signup(request):
    return render(request, 'vms/signup.html')


def index(request):
    return render(request, 'vms/index.html')


def vehicle(request):
    return render(request, 'vms/vehicle.html')


def driver(request):
    return render(request, 'vms/driver.html')


def fuel(request):
    return render(request, 'vms/fuel.html')


def booked(request):
    return render(request, 'vms/booked.html')


def vehicle_history(request):
    return render(request, 'vms/vehicle_history.html')


def report(request):
    return render(request, 'vms/report.html')


def full_report(request):
    return render(request, 'vms/full_report.html')


def contact(request):
    return render(request, 'vms/Contactus.html')


def logout(request):
    return redirect('/')
