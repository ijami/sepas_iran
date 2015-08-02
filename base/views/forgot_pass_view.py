__author__ = 'Ehsan'
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse


def forgot_pass(request):
    if request.user.is_authenticated():
        return redirect(reverse('home'))

    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('captcha')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("home")
        else:
            return render(request, 'base/login.html', {'errors': ["??? ????? ?? ??????? ?????? ???"]})

    return render(request, 'base/forgot_pass.html')
