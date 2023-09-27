from django.contrib.auth.models import User
from django.db import models


class AirlineCompany(models.Model):
    name = models.CharField(max_length=100)
    # Add more fields as needed

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='api_customer')
    # Add more fields as needed

    def __str__(self):
        return self.user.username


class Flight(models.Model):
    airline = models.ForeignKey(AirlineCompany, on_delete=models.CASCADE)
    origin_country = models.CharField(max_length=100)
    destination_country = models.CharField(max_length=100)
    date = models.DateField()
    # Add more fields as needed

    def __str__(self):
        return f"{self.origin_country} to {self.destination_country}"


class Ticket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    # Add more fields as needed

    def __str__(self):
        return f"Ticket #{self.pk}"
