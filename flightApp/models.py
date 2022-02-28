from statistics import mode
from tkinter import CASCADE
from django.db import models

# Flight model
# Passenger Model
# Reservation
class Flight(models.Model):
    flightNumber = models.CharField(max_length=10)
    operatingAirlines = models.CharField(max_length=50)
    departureCity = models.CharField(max_length=50)
    arrivalCity = models.CharField(max_length=50)
    dateOfDeparture = models.DateField()
    expectedTimeOfDeparture = models.TimeField()

    def __str__(self) -> str:
        return "{} ({}-{})".format(self.flightNumber , self.departureCity , self.arrivalCity)

class Passenger(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50 ,default='')
    email = models.CharField(max_length=50)
    phone= models.CharField(max_length=10)

    def __str__(self) -> str:
        return "{} {} {}".format(self.firstName , self.middleName , self.lastName)

class Reservation(models.Model):
    flight = models.OneToOneField(Flight , on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger , on_delete=models.CASCADE)

