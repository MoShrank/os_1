from .models import FutureLunch, User
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect


def user_is_lunch_author(function):
    def wrap(request, *args, **kwargs):
        f_lunch = FutureLunch.objects.get(pk=kwargs['lunch_id'])

        if f_lunch.user == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def users_profile(function):
    def wrap(request, *args, **kwargs):
        id = kwargs['user_id']

        if id == request.user.id:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    try:
        wrap.__name__ = function.__name__
    except Exception as e:
            pass
    try:
        wrap.__doc__ = function.__doc__
    except Exception as e:
            pass
    return wrap


def profile_complete(function):
    def wrap(request, *args, **kwargs):
        id = request.user.id
        u = User.objects.get(id=id)

        if u.first_name and u.last_name and u.meaning_of_life and u.picture:
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/profile/' + request.user.slug + '-' + str(id))
    try:
        wrap.__name__ = function.__name__
    except Exception as e:
            pass
    try:
        wrap.__doc__ = function.__doc__
    except Exception as e:
            pass
    return wrap
