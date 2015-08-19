__author__ = 'Mohsen'

from messaging.forms import NewMessageForm
from django.http import HttpResponse
from base.views.decorators import login_required
from messaging.models import Message
from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse

@login_required
def new_message_view(request):

    if request.method == 'GET':
        print('form method get')
        form = NewMessageForm
        return render(request, 'messaging/write.html', {
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


        return redirect(reverse('message_box'))


