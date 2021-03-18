from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm

# Create your views here.
def index(request):
    context_dict={'text':'Hello world!','number':100}
    return  render(request,'basic_app/index.html', context_dict)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')

def index2(request):
    context_dict={'text':'Test Template!','number':100}
    return render(request,'basic_app/index2.html', context_dict)

def register(request):
    
    registered= False

    if request.method == 'POST':
       user_form= UserForm(data=request.POST)
       profile_form=UserProfileInfoForm 

       if user_form.is_valid() and profile_form.is_valid():
           user=user_form.save()
           user.set_password(user.password)
           user.save()

           profile=profile_form.save(commit=False)
           profile.user=user

           if 'profile_pic' in request.FILES:
               profile.profile_pic=request.FILES['profile_pic']

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
