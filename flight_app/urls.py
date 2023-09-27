from django.contrib.auth.views import LoginView
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('flights/', views.flights, name='flights'),
    path('user/', views.user_page, name='user-page'),  # User page view
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='flight_app/login.html'), name='login'),  # Login view
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  # Logout view
    path('book-flight/<int:flight_id>/', views.book_flight, name='book-flight'),
    path('user/register/', views.register_view, name='user-register'),  # Register view
    path('user/login/', views.login_view, name='user-login'),  # Login view

    # API Endpoints
    # Flights
    path('api/flights/', views.FlightListAPIView.as_view(), name='flight-list'),
    path('api/flights/<int:pk>/', views.FlightDetailAPIView.as_view(), name='flight-detail'),

    # Customers
    path('api/customers/', views.CustomerListAPIView.as_view(), name='customer-list'),
    path('api/customers/<int:pk>/', views.CustomerDetailAPIView.as_view(), name='customer-detail'),

    # Airline Companies
    path('api/airline-companies/', views.AirlineCompanyListAPIView.as_view(), name='airline-company-list'),
    path('api/airline-companies/<int:pk>/', views.AirlineCompanyDetailAPIView.as_view(), name='airline-company-detail'),

    # Tickets
    path('api/tickets/', views.TicketListAPIView.as_view(), name='ticket-list'),
    path('api/tickets/<int:pk>/', views.TicketDetailAPIView.as_view(), name='ticket-detail'),

    # Users
    path('api/users/', views.UserListAPIView.as_view(), name='user-list'),
    path('api/users/<int:pk>/', views.UserDetailAPIView.as_view(), name='user-detail'),

    # User Registration
    path('api/register/', views.UserRegistrationAPIView.as_view(), name='user-registration'),
]
