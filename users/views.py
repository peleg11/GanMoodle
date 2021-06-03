from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from django.core.mail import send_mail

from .forms import ManagerForm, ParentForm,EditProfileForm,contactForm,supportMailForm, Video_form,Gallery_form
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from .models import GanGroup, User,contact_model, Video,Gallery

# Create your views here.
def index (request):
    return render(request,'homepage.html',context={})

def regpage (request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else :
        form=UserForm()
    return render(request,'regpage.html',{'form':form})


from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })

def register(request):
    return render(request, '../templates/register.html')


def manager_register (request):
    if request.method == 'POST':
        form = ManagerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else :
        form=ManagerForm(request.POST, request.FILES)
    return render(request,'../templates/manager_register.html',{'form':form})

def parent_register (request):
    if request.method == 'POST':
        form = ParentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else :
        form=ParentForm(request.POST, request.FILES)
    return render(request,'../templates/parent_register.html',{'form':form})

def edit_profile (request):
        if request.method == 'POST':
            form = EditProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('profile')
        else :
            form=EditProfileForm(request.POST,instance=request.user)
            return render(request,'edit_profile.html',{'form':form})


'''class manager_register(CreateView):
    model = User
    form_class = ManagerForm
    template_name = '../templates/manager_register.html'

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('homepage')
'''


def profile(request):
    user_form=request.user
    x=request.user.gangroups.all()
    return render(request,"../templates/profile.html", context={'user':user_form,'gangroups':x})



def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                messages.info(request, f"You are now logged in as ")
                return redirect('profile')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    return render(request, '../templates/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')


def support_page(request):
    form = supportMailForm()
    if request.method == 'POST':
        form = supportMailForm(request.POST)
        if form.is_valid:
            firstName = request.user.first_name
            lastName = request.user.last_name
            group= request.user.gangroups.all()
            subject = request.POST['subject']
            message = request.POST['message']
            if request.user.is_manager:
                recipient = ['admin_gan@gmail.com']
            elif request.user.is_parent:
                groupManager = User.objects.filter(is_manager=True,).filter(gangroups=group[0])

                recipient = [str(groupManager[0].email)] #TODO get specific manager mail for group
            send_mail(subject,message,from_email=firstName+" "+lastName+" from group: "+str(group[0]),
                        recipient_list=recipient)
            return render(request,"../templates/support_page.html",{"first_name":firstName})
    else:
        return render(request,"../templates/support_page.html",{"form":form})

def contact_info_view(request):
    data = contact_model.objects.all()
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
        else :
            form=contactForm(request.POST)
        return render(request,'contact.html',{'form':form,'data':data})

def delete_contact_view(request,pk):
    obj = contact_model.objects.get(pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    return render(request,'delete_contact.html',context={'obj':obj})

def delete_pic(request,pk):
    obj = Gallery.objects.get(pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    return render(request,'delete_pic.html',context={'obj':obj})


def video_index(request):
    all_video=Video.objects.all()
    gangrp=request.user.gangroups.all()[0]
    if request.method == "POST":
        form=Video_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form=form.save(commit=False)
            form.gangrp=request.user.gangroups.all()[0]
            form.save()
    else:
        form=Video_form()
    return render(request,'media.html',{"form":form,"all":all_video, "grp":str(gangrp)})

def gallery_index(request):
    all_pic=Gallery.objects.all()
    gangrp=request.user.gangroups.all()[0]
    if request.method == "POST":
        form=Gallery_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form=form.save(commit=False)
            form.gangrp=request.user.gangroups.all()[0]
            form.save()
    else:
        form=Gallery_form()
    return render(request,'gallery.html',{"form":form,"all":all_pic, "grp":str(gangrp)})

def view_my_group(request):

    group= request.user.gangroups.all()
    parents = User.objects.filter(is_parent=True).filter(gangroups=group[0])
    return render(request,'my_group.html',{ "parents":parents})

def delete_parent(request,pk):
    obj = User.objects.get(pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    return render(request,'remove_parent_from_group.html',context={'obj':obj})
