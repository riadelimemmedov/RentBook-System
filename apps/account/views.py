
#! Django function and methods
from django.shortcuts import render,get_object_or_404,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages


#!Models,Forms and Serializer classes
from .models import (Account)
from .forms import (AccountForm)

import json

# Create your views here.

#?register_account
@csrf_exempt
def register_account(request):
    if request.method == 'POST':
            form = AccountForm(request.POST or None)
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            gender = request.POST['gender'] if request.POST['gender'] != '' else ''
            account_type = request.POST['account_type'] if request.POST['account_type'] != '' else ''
            email = request.POST['email']
            phone = request.POST['phone']
            password = request.POST['password']
            
            user = Account.objects.create_user(first_name=first_name,last_name=last_name,gender=gender,account_type=account_type,email=email,phone=phone,password=password)
            user.save()
            messages.success(request,'Registration successfull.')
            return redirect(request.path)
        # json_data = json.loads(request.body.decode('utf-8'))
        # instance = Account.objects.create_user(first_name=json_data['first_name'],last_name=json_data['last_name'],gender=json_data['gender'],account_type=json_data['account_type'],email=json_data['email'],
        #                                         phone=json_data['phone'],password=json_data['password'])
        # instance.save()
        
        # requests.post("http://127.0.0.1:8000/account/login/",data={
        #     "email":json_data['email'],
        #     "password":json_data['password']
        # })
    else:
        form = AccountForm()

    return render(request,"account/register_login.html",context={
        'form':form
    })

#?login_account
@csrf_exempt
def login_account(request):
    if request.method == 'POST':
        raw_data = json.loads(request.body.decode('utf-8'))
        # account = authenticate(email="tural@mail.ru",password="c#11aaa!A")
        # if account is not None:
        #     print('Accout found')
        #     login(request,account)
        #     return redirect('home')
    return render(request,"account/register_login.html",context={})


#?login_account
def logout_account(request):
    pass
