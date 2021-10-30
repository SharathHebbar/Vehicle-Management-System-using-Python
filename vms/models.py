from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)


class Vehicle(models.Model):
    model = models.CharField(max_length=100)


class Driver(models.Model):
    name = models.CharField(max_length=100)


class Vehicle_history(models.Model):
    status = models.CharField(max_length=100)


class Booked(models.Model):
    status = models.CharField(max_length=100)


class Fuel(models.Model):
    type = models.CharField(max_length=100)


class Drives(models.Model):
    type = models.CharField(max_length=100)
