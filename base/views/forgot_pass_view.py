from django.contrib.auth.decorators import login_required
from base.views.send_mail import send_mail

__author__ = 'Ehsan'
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
import random
import string


def pass_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def forgot_pass(request):
    errors = []
    if request.user.is_authenticated():
        return redirect(reverse('home'))

    if request.method == 'POST':
        email = request.POST.get('email')
        captcha = request.POST.get('captcha')

        try:
            user = User.objects.get(email=email)
        except:
            errors.extend("کاربری با این پست التکرونیک ثبت نشده")
            return render(request, 'base/forgot_pass.html', {'errors': errors})

        else:
            if captcha == '19':
                new_pass = pass_generator()
                user.set_password(new_pass)
                user.save()
                send_mail('تغییر رمز عبور', 'b.i.sepasiran@gmail.com', [user.email], 'base/mail_new_pass.txt',
                          'base/mail_new_pass.html', {'user': user, 'new_pass': new_pass}, True)
                response = redirect(reverse('login'))
                response['Location'] += '?pass_changed=true'
                return response
            else:
                errors.extend("کد کپچای وارد شده نادرست است")
                return render(request, 'base/forgot_pass.html', {'errors': errors})

    return render(request, 'base/forgot_pass.html')
