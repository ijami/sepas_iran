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

def tourist_services_count(services):
    return services.__len__()

def tourist_services_used_count(services):
    counter = 0
    tours = services.objects.filter(instanceof=Tour)
    for tour in tours:
        if tour.going_date < datetime.now():
            counter = counter+1
    rooms = services.objects.filter(instanceof=Room)
    for room in rooms:
        if room < datetime.now():
            counter = counter+1
