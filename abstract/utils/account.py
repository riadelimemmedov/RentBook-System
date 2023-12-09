#

#!Django methods and functions
from django.shortcuts import redirect


# ?redirect_inactive_users
def redirect_inactive_users(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated and not request.user.is_active:
            return redirect(request.path)
        return view_func(request, *args, **kwargs)
    return wrapper


# ?throwMessage
def throwMessage(message_name):
    if message_name == "ACTIVE":
        return {
            "message": "Signed in successfully",
            "isLogin": "True",
            "icon": "success",
        }
    if message_name == "INACTIVE":
        return {
            "message": "Please activate your account",
            "isLogin": "False",
            "icon": "info",
        }
    if message_name == "INCORRECT":
        return {
            "message": "Email or Password incorrect",
            "isLogin": "False",
            "icon": "error",
        }


# ?setIsRememberMe
def setIsRememberMe(is_remember, request):
    if is_remember:
        request.session.set_expiry(0)
        request.session.modified = True
