from django.urls import path
from . import views
from .views import (
    FlightListAPIView,
    FlightDetailAPIView,
    CustomerListAPIView,
    CustomerDetailAPIView,
    AirlineCompanyListAPIView,
    AirlineCompanyDetailAPIView,
    TicketListAPIView,
    TicketDetailAPIView,
    UserListAPIView,
    UserDetailAPIView,
    UserRegistrationAPIView,
    UserRegistrationView
)

urlpatterns = [

    path('api-path1/', views.APIView1, name='api-path1'),
    path('api-path2/', views.APIView2, name='api-path2'),
    # Flights
    path('flights/', FlightListAPIView.as_view(), name='flight-list'),
    path('flights/<int:pk>/', FlightDetailAPIView.as_view(), name='flight-detail'),

    # Customers
    path('customers/', CustomerListAPIView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetailAPIView.as_view(), name='customer-detail'),

    # Airline Companies
    path('airline-companies/', AirlineCompanyListAPIView.as_view(), name='airline-company-list'),
    path('airline-companies/<int:pk>/', AirlineCompanyDetailAPIView.as_view(), name='airline-company-detail'),

    # Tickets
    path('tickets/', TicketListAPIView.as_view(), name='ticket-list'),
    path('tickets/<int:pk>/', TicketDetailAPIView.as_view(), name='ticket-detail'),

    # Users
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),

    # User Registration
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
]
