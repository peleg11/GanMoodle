from django.db import models
from django.contrib.auth.models import AbstractUser

class GanGroup(models.Model):

    name = models.CharField(max_length=128)


    def __str__(self):
        return self.name
    def __unicode__(self):
        return smart_unicode(self.name)

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    phone_number = models.CharField(max_length=10)
    gangroups = models.ManyToManyField(GanGroup)
    profile_pic = models.ImageField(upload_to='profilepics',null=True,blank=True)

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    police_cert = models.FileField(upload_to='policerts',null=True,blank=True)
    muni_cert = models.FileField(upload_to='municerts',null=True,blank=True)
    def __str__(self):
        return self.user.username

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    child_id = models.CharField(max_length=9)
<<<<<<< HEAD
=======


class contact_model(models.Model):
    parent_name = models.CharField(max_length=100,blank=False)
    child_name = models.CharField(max_length=100,blank=False)
    phone_number = models.IntegerField(blank=True,null=True)
    email = models.EmailField()

class GanGroup(models.Model):
    member=models.ManyToManyField(User)
    name = models.CharField(max_length=128)

    class Meta:
        ordering = ['name']
>>>>>>> cffaa68e2e209ee6f8350031d4cca03ff665847d

    def __str__(self):
        return self.user.username
