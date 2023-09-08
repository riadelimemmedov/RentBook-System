
#! Django function and methods
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import ListView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


#!Models,Forms and Serializer classes
from apps.book.models import Book,BookTitle



#?changeTheme
@csrf_exempt
def changeTheme(request):
    if 'is_dark_mode' in request.session:                                                                                       
        request.session['is_dark_mode'] = not request.session['is_dark_mode']
    else:
        request.session['is_dark_mode'] = True
    return JsonResponse({'is_dark_mode':request.session['is_dark_mode']})



#?HomeView
class HomeView(LoginRequiredMixin,TemplateView):
    template_name = "abstract/main.html"


#?DashboardView
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'abstract/dashboard.html'


#?AboutView
class AboutView(LoginRequiredMixin, TemplateView):
    template_name = 'abstract/about.html'


