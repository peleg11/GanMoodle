from django.shortcuts import render
from users.forms import UserForm

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
