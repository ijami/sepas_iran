from urllib.parse import urlunparse
from django.http.request import QueryDict
from django.http.response import HttpResponseRedirect

__author__ = 'Ehsan'

from functools import wraps
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.exceptions import PermissionDenied
from django.shortcuts import resolve_url
from django.utils import six
from django.utils.decorators import available_attrs
from django.utils.six.moves.urllib.parse import urlparse


def redirect_to_login(next, login_url=None,
                      redirect_field_name=REDIRECT_FIELD_NAME, type_code='login'):
    """
    Redirects the user to the login page, passing the given 'next' page
    """
    resolved_url = resolve_url(login_url or settings.LOGIN_URL)

    login_url_parts = list(urlparse(resolved_url))
    if redirect_field_name:
        querystring = QueryDict(login_url_parts[4], mutable=True)
        querystring[redirect_field_name] = next
        querystring['need'] = type_code
        login_url_parts[4] = querystring.urlencode(safe='/')

    return HttpResponseRedirect(urlunparse(login_url_parts))


def user_type_required(test_func, login_url=None, redirect_field_name=REDIRECT_FIELD_NAME, user_type=None):
    """
    Decorator for views that checks that the user passes the given test,
    redirecting to the log-in page if necessary. The test should be a callable
    that takes the user object and returns True if the user passes.
    """

    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated():
                if user_type is None or request.user.site_user.get_fields()['super_type'] == user_type:
                    return view_func(request, *args, **kwargs)
            path = request.build_absolute_uri()
            resolved_login_url = resolve_url(login_url or settings.LOGIN_URL)
            # If the login url is the same scheme and net location then just
            # use the path as the "next" url.
            login_scheme, login_netloc = urlparse(resolved_login_url)[:2]
            current_scheme, current_netloc = urlparse(path)[:2]
            if ((not login_scheme or login_scheme == current_scheme) and
                    (not login_netloc or login_netloc == current_netloc)):
                path = request.get_full_path()

            if user_type is None:
                type_code = 'login'
            else:
                type_code = user_type

            return redirect_to_login(
                path, resolved_login_url, redirect_field_name, type_code)

        return _wrapped_view

    return decorator

def login_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_type_required(
        lambda u: u.is_authenticated(),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def manager_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_type_required(
        lambda u: u.is_authenticated(),
        login_url=login_url,
        redirect_field_name=redirect_field_name,
        user_type="manager"
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def tourist_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_type_required(
        lambda u: u.is_authenticated(),
        login_url=login_url,
        redirect_field_name=redirect_field_name,
        user_type="tourist"
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def service_provider_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_type_required(
        lambda u: u.is_authenticated(),
        login_url=login_url,
        redirect_field_name=redirect_field_name,
        user_type="service_provider"
    )
    if function:
        return actual_decorator(function)
    return actual_decorator