from django.conf.urls import url
from basic_app import views
from django.urls import path
#Template tagging
app_name='basic_app'


urlpatterns=[
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),

]
