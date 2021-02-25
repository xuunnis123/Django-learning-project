from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord,User
from . import forms
# Create your views here.

def index(request):
    webpages_list=AccessRecord.objects.order_by('date')
    date_dict={'access_records':webpages_list} #mapping to templates/index.html <div>
    my_dict={'insert_me':"Hello I am coming from first_app/index.html"}
    return render(request,'first_app/index.html',context=date_dict)
def user(request):
    user_list=User.objects.order_by('first_name')
    user_dict={'users':user_list}
    return render(request,'first_app/user.html',context=user_dict)
def form_name_view(request):
    form=forms.FormName()
    if request.method=='POST':
        form=forms.FormName(request.POST)
        if form.is_valid():
            print("validation IS SUCCESS")
            print("Name="+form.cleaned_data['name'])
            print("Email="+form.cleaned_data['email'])
            print("Text="+form.cleaned_data['text'])
    return render(request,'first_app/form_page.html',{'form':form})
