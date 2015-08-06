from django.http.request import HttpRequest
from base.forms import LoginForm

__author__ = 'Iman'

from django.contrib.auth import logout, login, authenticate
from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse

import urllib.parse
import urllib.request


def logout_user(request):
    # api_key = '724F4F72774A6F384751442F504F6F724447734D4B413D3D'
    # url = 'http://api.kavenegar.com/v1/' + api_key + '/sms/send.json'
    #
    # values = {
    #     'receptor': "09127929708",
    #     'sender': '30006703323323',
    #     'type': '1',
    #     'message': "سلام. سامانه سپاس ایران به شما مرسی میگوید به خاطر اینکه هستید. ارسال شده از طریق کد. مسئول بخش تحقیق و توسعه :|"
    # }
    #
    # data = urllib.parse.urlencode(values)
    # binary_data = data.encode('utf-8')
    # sms_req = urllib.request.Request(url, binary_data)
    # sms_response = urllib.request.urlopen(sms_req)
    # print(sms_response.read())
    logout(request)
    return redirect(reverse('home'))


def login_user(request):
    print("salam")
    if request.user.is_authenticated():
        return redirect(reverse('home'))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                return redirect("home")
        else:
            return render(request, 'base/login.html', {'errors': ["نام کابری یا گذرواژه اشتباه است"]})

    return render(request, 'base/login.html')
