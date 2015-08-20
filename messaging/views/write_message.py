__author__ = 'Mohsen'

from messaging.forms import NewMessageForm
from django.http import HttpResponse
from base.views.decorators import tourist_required, manager_required, service_provider_required
from messaging.models import Message
from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse

@tourist_required()
def tourist_new_message_view(request):

    if request.method == 'GET':
        print('form method get')
        form = NewMessageForm
        return render(request, 'messaging/tourist_write.html', {
            'form': form
        })

    elif request.method == 'POST':
        usern = request.user.site_user
        form = NewMessageForm(request.POST)
        if form.is_valid():

            text = form.cleaned_data['text']
            receiver = form.cleaned_data['receiver']
            header = form.cleaned_data['header']

            message = Message(text=text, receiver=receiver, header=header, sender=usern)

            message.save()
        else:
            return HttpResponse(form.errors)


        return redirect(reverse('tourist_message_box'))

@service_provider_required()
def service_provider_new_message_view(request):

    if request.method == 'GET':
        print('form method get')
        form = NewMessageForm
        return render(request, 'messaging/service_provider_write.html', {
            'form': form
        })

    elif request.method == 'POST':
        usern = request.user.site_user
        form = NewMessageForm(request.POST)
        if form.is_valid():

            text = form.cleaned_data['text']
            receiver = form.cleaned_data['receiver']
            header = form.cleaned_data['header']

            message = Message(text=text, receiver=receiver, header=header, sender=usern)

            message.save()
        else:
            return HttpResponse(form.errors)


        return redirect(reverse('service_provider_message_box'))

@manager_required()
def manager_new_message_view(request):

    if request.method == 'GET':
        print('form method get')
        form = NewMessageForm
        return render(request, 'messaging/manager_write.html', {
            'form': form
        })

    elif request.method == 'POST':
        usern = request.user.site_user
        form = NewMessageForm(request.POST)
        if form.is_valid():

            text = form.cleaned_data['text']
            receiver = form.cleaned_data['receiver']
            header = form.cleaned_data['header']

            message = Message(text=text, receiver=receiver, header=header, sender=usern)

            message.save()
        else:
            return HttpResponse(form.errors)


        return redirect(reverse('manager_message_box'))

