from django import forms
from django.contrib.auth.models import User
from basic.models import Userprofileinfo

class Userform(forms.ModelForm):

    password = forms.CharField(widget= forms.PasswordInput())

    class Meta():
        model= User
        fields= ('username', 'email', 'password')



class Userprofileform(forms.ModelForm):
    class Meta():
        model = Userprofileinfo
        fields= ('porfolio_sit', 'profile_pic')