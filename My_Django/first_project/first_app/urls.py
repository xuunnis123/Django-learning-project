from django.conf.urls import url
from first_app import views

urlpatterns=[
    url('',views.index,name='index'),
    url('/user',views.user,name='user'),
    url('/userAddUser',views.addUser,name='addUser'),
    ]
