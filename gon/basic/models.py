from django.db import models
from django.contrib.auth.models import User

class Userprofileinfo(models.Model):

    user = models.OneToOneField(User)


    porfolio_sit = models.URLField(blank = True)
    profile_pic=models.ImageField(upload_to='profile_pics' , blank=True)


    def __str__(self):
        return self.user.username
# Create your models here.
