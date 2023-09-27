from .models import User, Customer, AirlineCompany, Country, Flight, Ticket, Administrator
from django.contrib.auth import authenticate, login
from business_logic import LoginToken

class FacadeBase:
    def __init__(self, user):
        self.user = user

    def get_all_flights(self):
        return Flight.objects.all()

    def get_flight_by_id(self, id):
        try:
            return Flight.objects.get(id=id)
        except Flight.DoesNotExist:
            return None

    def get_flights_by_parameters(self, origin_country_id, destination_country_id, date):
        return Flight.objects.filter(
            origin_country_id=origin_country_id,
            destination_country_id=destination_country_id,
            departure_time__date=date
        )

    def get_all_airlines(self):
        return AirlineCompany.objects.all()

    def get_airline_by_id(self, id):
        try:
            return AirlineCompany.objects.get(id=id)
        except AirlineCompany.DoesNotExist:
            return None

    def get_airline_by_parameters(self, country_id):
        return AirlineCompany.objects.filter(country_id=country_id)

    def get_all_countries(self):
        return Country.objects.all()

    def get_country_by_id(self, id):
        try:
            return Country.objects.get(id=id)
        except Country.DoesNotExist:
            return None

    def create_new_user(self, user):
        return User.objects.create(**user)

class AnonymousFacade(FacadeBase):
    def login(self, username, password):
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            login_token = LoginToken(id=user.id, name=user.username, role='anonymous')
            return self.get_facade(user, login_token)
        else:
            return None

class CustomerFacade(AnonymousFacade):
    def __init__(self, user, login_token):
        super().__init__(user)
        self.login_token = login_token

    def update_customer(self, customer_id, data):
        if self.login_token.id == customer_id and self.login_token.role == 'customer':
            customer = Customer.objects.get(id=customer_id)
            for key, value in data.items():
                setattr(customer, key, value)
            customer.save()
            return customer
        else:
            raise PermissionError("You are not authorized to update this customer")

    def add_ticket(self, customer_id, flight_id):
        if self.login_token.id == customer_id and self.login_token.role == 'customer':
            customer = Customer.objects.get(id=customer_id)
            flight = Flight.objects.get(id=flight_id)
            ticket = Ticket.objects.create(customer=customer, flight=flight)
            return ticket
        else:
            raise PermissionError("You are not authorized to add a ticket")

    def remove_ticket(self, ticket_id):
        if self.login_token.role == 'customer':
            try:
                ticket = Ticket.objects.get(id=ticket_id)
                if ticket.customer_id == self.login_token.id:
                    ticket.delete()
                    return True
                else:
                    raise PermissionError("You are not authorized to remove this ticket")
            except Ticket.DoesNotExist:
                return False
        else:
            raise PermissionError("You are not authorized to remove this ticket")

    def get_my_tickets(self, customer_id):
        if self.login_token.id == customer_id and self.login_token.role == 'customer':
            customer = Customer.objects.get(id=customer_id)
            tickets = Ticket.objects.filter(customer=customer)
            return tickets
        else:
            raise PermissionError("You are not authorized to get tickets for this customer")

class AirlineFacade(AnonymousFacade):
    def __init__(self, user, login_token):
        super().__init__(user)
        self.login_token = login_token

    def get_my_flights(self, airline_id):
        if self.login_token.id == airline_id and self.login_token.role == 'airline':
            airline = AirlineCompany.objects.get(id=airline_id)
            flights = Flight.objects.filter(airline=airline)
            return flights
        else:
            raise PermissionError("You are not authorized to get flights for this airline")

    def update_airline(self, airline_id, data):
        if self.login_token.id == airline_id and self.login_token.role == 'airline':
            airline = AirlineCompany.objects.get(id=airline_id)
            for key, value in data.items():
                setattr(airline, key, value)
            airline.save()
            return airline
        else:
            raise PermissionError("You are not authorized to update this airline")

    def add_flight(self, airline_id, data):
        if self.login_token.id == airline_id and self.login_token.role == 'airline':
            airline = AirlineCompany.objects.get(id=airline_id)
            flight = Flight.objects.create(airline=airline, **data)
            return flight
        else:
            raise PermissionError("You are not authorized to add a flight")

    def update_flight(self, flight_id, data):
        if self.login_token.role == 'airline':
            flight = Flight.objects.get(id=flight_id)
            if flight.airline_id == self.login_token.id:
                for key, value in data.items():
                    setattr(flight, key, value)
                flight.save()
                return flight
            else:
                raise PermissionError("You are not authorized to update this flight")
        else:
            raise PermissionError("You are not authorized to update flights")

    def remove_flight(self, flight_id):
        if self.login_token.role == 'airline':
            flight = Flight.objects.get(id=flight_id)
            if flight.airline_id == self.login_token.id:
                try:
                    flight.delete()
                    return True
                except Flight.DoesNotExist:
                    return False
            else:
                raise PermissionError("You are not authorized to remove this flight")
        else:
            raise PermissionError("You are not authorized to remove flights")

class AdministratorFacade(AnonymousFacade):
    def __init__(self, user, login_token):
        super().__init__(user)
        self.login_token = login_token

    def get_all_customers(self):
        if self.login_token.role == 'administrator':
            return Customer.objects.all()
        else:
            raise PermissionError("You are not authorized to get all customers")

    def add_airline(self, user, country_id):
        if self.login_token.role == 'administrator':
            airline = AirlineCompany.objects.create(user=user, country_id=country_id)
            return airline
        else:
            raise PermissionError("You are not authorized to add an airline")

    def add_customer(self, user):
        if self.login_token.role == 'administrator':
            customer = Customer.objects.create(user=user)
            return customer
        else:
            raise PermissionError("You are not authorized to add a customer")

    def add_administrator(self, user):
        if self.login_token.role == 'administrator':
            administrator = Administrator.objects.create(user=user)
            return administrator
        else:
            raise PermissionError("You are not authorized to add an administrator")

    def remove_airline(self, airline_id):
        if self.login_token.role == 'administrator':
            try:
                airline = AirlineCompany.objects.get(id=airline_id)
                airline.delete()
                return True
            except AirlineCompany.DoesNotExist:
                return False
        else:
            raise PermissionError("You are not authorized to remove this airline")

    def remove_customer(self, customer_id):
        if self.login_token.role == 'administrator':
            try:
                customer = Customer.objects.get(id=customer_id)
                customer.delete()
                return True
            except Customer.DoesNotExist:
                return False
        else:
            raise PermissionError("You are not authorized to remove this customer")

    def remove_administrator(self, administrator_id):
        if self.login_token.role == 'administrator':
            try:
                administrator = Administrator.objects.get(id=administrator_id)
                administrator.delete()
                return True
            except Administrator.DoesNotExist:
                return False
        else:
            raise PermissionError("You are not authorized to remove this administrator")
