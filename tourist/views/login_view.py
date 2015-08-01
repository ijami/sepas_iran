__author__ = 'Iman'

from django.contrib.auth import logout
from django.shortcuts import redirect, render

def logout_view(request):
    logout(request)
    return redirect('/')

def login_view(request):
    if request.method == 'POST':
        pass
    return render(request, 'tourist/login.html')
