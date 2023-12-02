#

#!Django methods and functions
from django.shortcuts import redirect


#?redirect_inactive_users
def redirect_inactive_users(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated and not request.user.is_active:
            return redirect(request.path)
        return view_func(request, *args, **kwargs)
    return wrapper