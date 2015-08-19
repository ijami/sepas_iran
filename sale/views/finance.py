from datetime import datetime

from tourist.models import Tourist
from sale.models import ServiceItem, Factor
from service.models import Tour, Room, Flight


def dashboard_report(start, end, service_type):
    services_items = tourist_services_all()
    output = []
    for service_item in services_items:
        service = service_item.service
        if service_type % 2 == 0 and isinstance(service, Tour):
            if service.going_date <= end:
                if service.going_date >= start:
                    output.append(service_item)
        elif service_type % 5 == 0 and isinstance(service, Room):
            if service.end_date <= end:
                if service.end_date >= start:
                    output.append(service_item)
        elif service_type % 3 == 0 and isinstance(service, Flight):
            if service.date <= end:
                if service.date >= start:
                    output.append(service_item)
    return output



def tourist_services_all():
    factors = Factor.objects.all()
    items = []
    for factor in factors:
        service_items = factor.items.all()
        for serviceItem in service_items:
            items.append(serviceItem)
    return items



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
        if isinstance(service, Tour):
            if service.going_date < datetime.now():
                output.append(service)
        elif isinstance(service, Room):
            if service.end_date < datetime.now():
                output.append(service)
        elif isinstance(service, Flight):
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
        if isinstance(service, Flight):
            if service.going_date > datetime.now():
                output.append(service)
    return output

def tourist_services_price(tourist_id):
    services = tourist_services(tourist_id)
    price = 0
    for service in services:
        price += service.price
    return price

