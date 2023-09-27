from .models import User, Customer, AirlineCompany, Country, Flight, Ticket
from django.db.models import Q
from django.utils import timezone
from datetime import timedelta
import logging

logger = logging.getLogger(__name__)


class DataAccessLayer:
    def get_by_id(self, model, _id):
        try:
            result = model.objects.get(id=_id)
            logger.info(f"Retrieved {model.__name__} with id {_id}")
            return result
        except model.DoesNotExist:
            logger.error(f"{model.__name__} with id {_id} does not exist.")
            return None

    def get_all(self, model):
        try:
            results = model.objects.all()
            logger.info(f"Retrieved all records from {model.__name__}")
            return results
        except Exception as e:
            logger.error(str(e))
            return None

    def add(self, model, data):
        try:
            instance = model(**data)
            instance.save()
            logger.info(f"Added a new record to {model.__name__}")
            return instance
        except Exception as e:
            logger.error(str(e))
            return None

    def update(self, model, _id, data):
        try:
            instance = model.objects.get(id=_id)
            for (key, value) in data.items():
                setattr(instance, key, value)
            instance.save()
            logger.info(f"Updated {model.__name__} with id {_id}")
            return instance
        except model.DoesNotExist:
            logger.error(f"{model.__name__} with id {_id} does not exist.")
            return None

    def remove(self, model, _id):
        try:
            instance = model.objects.get(id=_id)
            instance.delete()
            logger.info(f"Removed {model.__name__} with id {_id}")
        except model.DoesNotExist:
            logger.error(f"{model.__name__} with id {_id} does not exist.")
            return None

    def getAirlinesByCountry(self, country_id):
        try:
            airlines = AirlineCompany.objects.filter(country_id=country_id)
            logger.info(f"Retrieved airlines by country id {country_id}")
            return airlines
        except Exception as e:
            logger.error(str(e))
            return None

    def getFlightsByOriginCountryId(self, country_id):
        try:
            flights = Flight.objects.filter(origin_country_id=country_id)
            logger.info(f"Retrieved flights by origin country id {country_id}")
            return flights
        except Exception as e:
            logger.error(str(e))
            return None

    def getFlightsByDestinationCountryId(self, country_id):
        try:
            flights = Flight.objects.filter(destination_country_id=country_id)
            logger.info(f"Retrieved flights by destination country id {country_id}")
            return flights
        except Exception as e:
            logger.error(str(e))
            return None

    def getFlightsByDepartureDate(self, date):
        try:
            flights = Flight.objects.filter(departure_time__date=date)
            logger.info(f"Retrieved flights by departure date {date}")
            return flights
        except Exception as e:
            logger.error(str(e))
            return None

    def getFlightsByLandingDate(self, date):
        try:
            flights = Flight.objects.filter(arrival_time__date=date)
            logger.info(f"Retrieved flights by landing date {date}")
            return flights
        except Exception as e:
            logger.error(str(e))
            return None

    def getFlightsByCustomer(self, customer_id):
        try:
            customer = Customer.objects.get(id=customer_id)
            tickets = Ticket.objects.filter(customer=customer)
            flights = [ticket.flight for ticket in tickets]
            logger.info(f"Retrieved flights by customer id {customer_id}")
            return flights
        except Exception as e:
            logger.error(str(e))
            return None

