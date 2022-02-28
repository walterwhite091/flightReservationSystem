from flightApp.models import Flight , Reservation , Passenger
from flightApp.serializer import  FlightSerializer , ReservationSerializer , PassengerSerializer

from rest_framework.viewsets import ModelViewSet
# Create your views here.

class Flight(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class Passenger(ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer 

class Reservation(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer 
