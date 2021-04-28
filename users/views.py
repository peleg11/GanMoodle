from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .forms import ManagerForm, ParentForm,EditProfileForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User

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
	user_form = request.user
	#profile_form = ProfileForm(instance=request.user.profile)
	return render(request,"../templates/profile.html", context={'user':user_form})


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
