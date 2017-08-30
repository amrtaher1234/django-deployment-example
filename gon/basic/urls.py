from django.conf.urls import url 
from basic import views

app_name='basic'
urlpatterns = [
    url(r'^register/$' , views.register , name='register'),
    url(r'^userlogin/$' , views.user_login , name='login'),

]