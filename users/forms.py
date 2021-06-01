from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.db import transaction
from .models import User,Manager,Parent,contact_model,GanGroup, Video, Gallery
from django.forms import ModelForm


class ManagerForm(UserCreationForm):
    first_name=forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    #email=forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    #groups =forms.CharField(required=True)

    profile_pic = forms.ImageField(required=False)
    police_cert=forms.FileField(required=False)
    muni_cert=forms.FileField(required=False)

    class Meta:
        model=User

        fields=('first_name','username','last_name','email', 'phone_number',
                'profile_pic','police_cert','muni_cert','password1','password2')



#    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_manager = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.phone_number=self.cleaned_data.get('phone_number')
        #user.gangroups.add('gangroups')
        profile_pic=self.cleaned_data.get('profile_pic')
        user.is_active=False
        user.save()
        manager = Manager.objects.create(user=user)
        manager.police_cert=self.cleaned_data.get('police_cert')
        manager.muni_cert=self.cleaned_data.get('muni_cert')
        manager.save()
        return user

class ParentForm(UserCreationForm):
        first_name=forms.CharField(required=True)
        last_name=forms.CharField(required=True)
        phone_number = forms.CharField(required=True)
        profile_pic = forms.ImageField(required=False)
        child_id=forms.CharField()

        class Meta:
            model=User
            model1=GanGroup
            fields=('first_name','last_name','username','email', 'phone_number',
                    'profile_pic','child_id','password1','password2','gangroups')

        #@transaction.atomic
        def save(self):
            user = super().save(commit=False)
            gangroups=self.cleaned_data.get('gangroups')
            print(gangroups[0])
            #a=gangroups.tolist()
            #print(a)
            # group = GanGroup.objects.get(name='First')

            user.is_parent = True
            user.first_name = self.cleaned_data.get('first_name')
            user.last_name = self.cleaned_data.get('last_name')
            user.phone_number=self.cleaned_data.get('phone_number')
            profile_pic=self.cleaned_data.get('profile_pic')
            user.save()
            user.gangroups.add(gangroups[0])
            parent = Parent.objects.create(user=user)
            parent.child_id=self.cleaned_data.get('child_id')
            parent.save()
            return user

class EditProfileForm(UserChangeForm ):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    phone_number = forms.CharField(required=True)
    profile_pic = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('first_name','last_name', 'phone_number','profile_pic')
        #exclude = ('user',)

class contactForm(ModelForm):
    class Meta:
        model = contact_model
        fields = ('parent_name','child_name','phone_number','email')

class supportMailForm(forms.Form):
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class Video_form(forms.ModelForm):
    class Meta:
        model=Video
        exclude=['gangrp']
        #gangrp=forms.CharField(queryset=User.gangroups.objects.all())
        fields=("caption","video","gangrp")

class Gallery_form(forms.ModelForm):
    class Meta:
        model=Gallery
        exclude=['gangrp']
        #gangrp=forms.CharField(queryset=User.gangroups.objects.all())
        fields=("caption","pic","gangrp")
