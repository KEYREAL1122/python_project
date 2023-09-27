from django.db import models
from django.utils import timezone
from datetime import timedelta


class AirlineCompany(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Administrator(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Customer(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Flight(models.Model):
    airline = models.ForeignKey(AirlineCompany, on_delete=models.CASCADE)
    origin_country = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='departure_flights')
    destination_country = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='arrival_flights')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    @classmethod
    def get_by_parameters(cls, origin_country_id, destination_country_id, date):
        return cls.objects.filter(
            origin_country_id=origin_country_id,
            destination_country_id=destination_country_id,
            date=date
        )

    @classmethod
    def get_by_airline_id(cls, airline_id):
        return cls.objects.filter(airline_id=airline_id)

    @classmethod
    def get_arrival_flights(cls, country_id):
        now = timezone.now()
        in_12_hours = now + timedelta(hours=12)
        return cls.objects.filter(destination_country_id=country_id, arrival_time__range=(now, in_12_hours))

    @classmethod
    def get_departure_flights(cls, country_id):
        now = timezone.now()
        in_12_hours = now + timedelta(hours=12)
        return cls.objects.filter(origin_country_id=country_id, departure_time__range=(now, in_12_hours))

    def __str__(self):
        return f"{self.origin_country} to {self.destination_country}"


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    @classmethod
    def get_by_customer(cls, customer_id):
        return cls.objects.filter(customer_id=customer_id)

    def __str__(self):
        return f"Ticket #{self.pk}"
