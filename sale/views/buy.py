__author__ = 'MJR'
from base.views.decorators import tourist_required

@tourist_required()
def buy(request):
    pass