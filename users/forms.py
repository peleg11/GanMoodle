from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.db import transaction
from .models import User,Manager,Parent

class ManagerForm(UserCreationForm):
    first_name=forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    #email=forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    group =forms.CharField(required=True)
    profile_pic = forms.ImageField(required=False)
    police_cert=forms.FileField(required=False)
    muni_cert=forms.FileField(required=False)

    class Meta:
        model=User
        fields=('first_name','username','last_name','email', 'phone_number', 'group',
                'profile_pic','police_cert','muni_cert','password1','password2')

#    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_manager = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.phone_number=self.cleaned_data.get('phone_number')
        user.group=self.cleaned_data.get('group')
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
        #email=forms.EmailField(required=True)
        phone_number = forms.CharField(required=True)
        group =forms.CharField(required=True)
        profile_pic = forms.ImageField(required=False)
        child_id=forms.CharField()

        class Meta:
            model=User
            fields=('first_name','last_name','username','email', 'phone_number', 'group',
                    'profile_pic','child_id','password1','password2')

        #@transaction.atomic
        def save(self):
            user = super().save(commit=False)
            user.is_parent = True
            user.first_name = self.get('first_name')
            user.last_name = self.cleaned_data.get('last_name')
            user.phone_number=self.cleaned_data.get('phone_number')
            user.group=self.cleaned_data.get('group')
            profile_pic=self.cleaned_data.get('profile_pic')
            user.save()
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
