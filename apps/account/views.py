
#! Django function and methods
from django.shortcuts import render,get_object_or_404,redirect

#!Models,Forms and Serializer classes


# Create your views here.


#?register_account
def register_account(request):
    return render(request,"account/register_login.html",context={})

#?login_account
def login_account(request):
    return render(request,"account/register_login.html",context={})

#?login_account
def logout_account(request):
    pass
