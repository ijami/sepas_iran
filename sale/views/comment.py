from django.core.exceptions import ObjectDoesNotExist

__author__ = 'MJR'
from django.shortcuts import render, redirect
from service.models import Service, Comment
from django.http import Http404
from sale.models import Factor, ServiceItem
from django.core.urlresolvers import reverse
import datetime
from base.views.decorators import login_required

@login_required()
def add_comment(request):
    if request.method == "POST":
        user = request.user.site_user
        text = request.POST['comment']
        date = datetime.datetime.now()
        service = Service.objects.get(sold_number=request.POST['sn'])
        comment = Comment()
        comment.service = service
        comment.send_time = date
        comment.sender = user
        comment.text = text
        comment.save()
        url = '/sale/service/' + service.sold_number
        print(url)
        return redirect(url)


