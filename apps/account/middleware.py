
#! Django function and methods
from django.shortcuts import redirect
from django.urls import reverse


#*RedirectAuthenticatedMiddleware
class RedirectAuthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code that is executed in each request before the view is called
        if request.user.is_authenticated:
            if request.path == reverse('account:login_account') or request.path == reverse('account:register_account'):
                return redirect('dashboard')
        # Code that is executed in each request after the view is called
        response = self.get_response(request)
        return response