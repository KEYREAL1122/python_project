from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from ..forms import UserRegisterForm
from .models import AirlineCompany, Customer, Flight, Ticket
from ..api.serializers import (
    AirlineCompanySerializer,
    CustomerSerializer,
    UserSerializer,
    FlightSerializer,
    TicketSerializer,
    UserRegistrationSerializer,
)

# If you want to register your models to the admin site, you can do so here, like so:

from django.contrib import admin
from .models import AirlineCompany, Customer, Flight, Ticket

admin.site.register(AirlineCompany)
admin.site.register(Customer)
admin.site.register(Flight)
admin.site.register(Ticket)

