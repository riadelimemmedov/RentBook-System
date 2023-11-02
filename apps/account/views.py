
#! Django function and methods
from django.shortcuts import render,get_object_or_404,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,authenticate,logout

import time

#!Models,Forms and Serializer classes

import json
from .models import Account
from django.contrib.auth.models import User
import requests


# Create your views here.

#?register_account
@csrf_exempt
def register_account(request):
    # instance = Account.objects.create_user(first_name="Tural",last_name="Valiyev",gender="MALE",account_type="SELLER",email="tural@mail.ru",phone="231321321321",password="hd266313")
    if request.method == 'POST':
        json_data = json.loads(request.body.decode('utf-8'))
        instance = Account.objects.create_user(first_name=json_data['first_name'],last_name=json_data['last_name'],gender=json_data['gender'],account_type=json_data['account_type'],email=json_data['email'],
                                                phone=json_data['phone'],password=json_data['password'])
        instance.save()
        
        requests.post("http://127.0.0.1:8000/account/login/",data={
            "email":json_data['email'],
            "password":json_data['password']
        })        
    return render(request,"account/register_login.html",context={})

#?login_account
def login_account(request):
    if(request.method == 'POST'):
        print('Post request come from login url ', request.path)
    return render(request,"account/register_login.html",context={})


#?login_account
def logout_account(request):
    pass
