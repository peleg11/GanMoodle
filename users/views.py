from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .forms import ManagerForm, ParentForm
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


#def manager_register (request):
#    if request.method == 'POST':
#        form = ManagerForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('homepage')
#    else :
#        form=ManagerForm()
#    return render(request,'../templates/manager_register.html',{'form':form})

class parent_register(CreateView):
    model = User
    form_class = ParentForm
    template_name = '../templates/parent_register.html'

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('homepage')

class manager_register(CreateView):
    model = User
    form_class = ManagerForm
    template_name = '../templates/manager_register.html'

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('homepage')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, '../templates/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')
