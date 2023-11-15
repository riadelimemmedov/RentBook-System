
#! Django function and methods
from django.shortcuts import render,get_object_or_404,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse


#!Models,Forms and Serializer classes
from .models import (Account)
from .forms import (AccountForm)


#!Python modules and function
import time
# Create your views here.

#?register_account
def register_account(request):
    #If user email,phone already exists database return client to message
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
            print('Creating user is ', user)
            user.save()
            messages.success(request,'Registration successfull.')
            return redirect(request.path)
    else:
        form = AccountForm()

    return render(request,"account/register_login.html",context={
        'form':form
    })

#?login_account
@csrf_exempt
def login_account(request):
    #If user or password incorrect return message to client
    if request.method == 'POST' and request.POST.get('csrf') != '':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(email=email,password=password)
        if user is not None:
            login(request,user)
            return JsonResponse({'message':'Signed in successfully','isLogin':'True','icon':'success'})
        else:
            return JsonResponse({'message':'Email or Password incorrect','isLogin':'False','icon':'error'})            
    return render(request,"account/register_login.html",context={})


#?login_account
@login_required(login_url='account:login_account')
def logout_account(request):
    logout(request)
    messages.add_message(request,messages.SUCCESS,'You are logged out.')
    return redirect('account:login_account')
