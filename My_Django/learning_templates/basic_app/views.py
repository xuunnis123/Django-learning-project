from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm

#
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

import logging
# Create your views here.
def index(request):
    context_dict={'text':'Hello world!','number':100}
    return  render(request,'basic_app/index.html', context_dict)

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('basic_app:user_login'))


def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')

def index2(request):
    context_dict={'text':'Test Template!','number':100}
    return render(request,'basic_app/index2.html', context_dict)

def register(request):
    
    registered= False
    logging.error(request.method)
    if request.method == 'POST':
       user_form= UserForm(data=request.POST)
       profile_form=UserProfileInfoForm(request.POST)
       logging.error(user_form) 
       if user_form.is_valid() and profile_form.is_valid():
           user=user_form.save()
           
           user.set_password(user.password)
           user.save()

           profile=profile_form.save(commit=False)
           profile.user=user

           if 'profile_pics' in request.FILES:
               profile.profile_pic=request.FILES['profile_pics']

           profile.save()
           
           registered=True
       else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    
    return render(request,'basic_app/registeration.html',
    {'user_form':user_form,
    'profile_form':profile_form,
    'registered':registered})

def user_login(request):
    
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username,password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed!")
            print("Username:{} and password:{}".format(username,password))
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request,'basic_app/login.html',{})