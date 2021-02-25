from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord,User

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
