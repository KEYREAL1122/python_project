from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from .models import AirlineCompany, Customer, Flight, Ticket
from .forms import UserRegisterForm
from .api_service import get_all_users
from .api.serializers import (
    AirlineCompanySerializer,
    CustomerSerializer,
    UserSerializer,
    FlightSerializer,
    TicketSerializer,
    UserRegistrationSerializer,
)

def home(request):
    return render(request, 'flight_app/home.html')

def list_users(request):
    users = get_all_users()
    return render(request, 'flight_app/list_users.html', {'users': users})

def flights(request):
    flights_list = Flight.objects.all()
    return render(request, 'flight_app/flights.html', {'flights': flights_list})

@login_required(login_url='login')
def user_page(request):
    flights = Flight.objects.all()
    return render(request, 'flight_app/user_page.html', {'flights': flights})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'flight_app/login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'flight_app/login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
        else:
            errors = form.errors
            return render(request, 'flight_app/register.html', {'form': form, 'errors': errors})
    else:
        form = UserRegisterForm()
        return render(request, 'flight_app/register.html', {'form': form})

@login_required(login_url='login')
def book_flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    user = request.user
    
    # Check if a ticket already exists.
    existing_ticket = Ticket.objects.filter(flight=flight, owner=user).first()
    if not existing_ticket:
        Ticket.objects.create(flight=flight, owner=user)
        return redirect('user-detail', pk=user.id)
    else:
        return render(request, 'flight_app/error.html', {'message': 'You already have a ticket for this flight!'})

class AirlineCompanyListAPIView(generics.ListAPIView):
    queryset = AirlineCompany.objects.all()
    serializer_class = AirlineCompanySerializer

class AirlineCompanyDetailAPIView(generics.RetrieveAPIView):
    queryset = AirlineCompany.objects.all()
    serializer_class = AirlineCompanySerializer

class CustomerListAPIView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailAPIView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FlightListAPIView(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class FlightDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TicketListAPIView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketDetailAPIView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class UserRegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
