__author__ = 'Ehsan'
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


def forgot_pass(request):
    errors = []
    if request.user.is_authenticated():
        return redirect(reverse('home'))

    if request.method == 'POST':
        email = request.POST.get('email')
        captcha = request.POST.get('captcha')

        user = User.objects.filter(email=email)
        if user.count() != 1:
            errors.extend("????? ???? ??? ?? ?????? ??? ????")
            return render(request, 'base/forgot_pass.html', {'errors': errors})

        else:
            if captcha == '21':
                user.set_password("new")
                return redirect(reverse('login'))
            else:
                errors.extend("?? ???? ?? ???? ???? ????")
                return render(request, 'base/forgot_pass.html', {'errors': errors})


    return render(request, 'base/forgot_pass.html')
