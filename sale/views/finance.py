from tourist.models import Tourist
from sale.models import ServiceItem,Factor
from service.models import Tour,Room,Flight
from datetime import datetime, timedelta, timezone

def tourist_services(tourist_id):
    tourist = Tourist.objects.filter(id=tourist_id)
    factors = Factor.objects.filter(tourist=tourist)
    services =[]
    for factor in factors:
        serviceItems = ServiceItem.objects.filter(factor=factor).all()
        for serviceItem in serviceItems:
            services.append(serviceItem)
    return services

def tourist_services_used(tourist_id):
    services = tourist_services(tourist_id)
    output = []
    # tours = services.filter(instanceof=Tour)
    for service in services:
        if isinstance(service,Tour):
            if service.going_date < datetime.now():
                output.append(service)
        elif isinstance(service,Room):
            if service.end_date < datetime.now():
                output.append(service)
        elif isinstance(service,Flight):
            if service.date < datetime.now():
                output.append(service)
    return output
    #
    # rooms = services.filter(instanceof=Room)
    # for room in rooms:
    #     if room.end_date < datetime.now():
    #         counter = counter+1
    # flights = services.filter(instanceof=Flight)
    # for flight in flights:
    #     if flight.date < datetime.now():
    #         counter = counter+1


def tourist_services_waited(tourist_id):
    services = tourist_services(tourist_id)
    output = []
    # tours = services.filter(instanceof=Tour)
    for service in services:
        if isinstance(service,Tour):
            if service.going_date > datetime.now():
                output.append(service)
        elif isinstance(service,Room):
            if service.start_date > datetime.now():
                output.append(service)
        elif isinstance(service,Flight):
            if service.date > datetime.now():
                output.append(service)
    return output

def tourist_tours(tourist_id):
    services = tourist_services(tourist_id)
    output=[]
    for service in services:
        if isinstance(service,Tour):
            if service.going_date > datetime.now():
                output.append(service)
    return output

def tourist_rooms(tourist_id):
    services = tourist_services(tourist_id)
    output=[]
    for service in services:
        if isinstance(service,Room):
            if service.going_date > datetime.now():
                output.append(service)
    return output


def tourist_flights(tourist_id):
    services = tourist_services(tourist_id)
    output=[]
    for service in services:
        if isinstance(service,Flight):
            if service.going_date > datetime.now():
                output.append(service)
    return output

def tourist_services_price(tourist_id):
    services = tourist_services(tourist_id)
    price =0
    for service in services:
        price += service.price
    return price

