from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,'homepage.html',context={})

def regpage (request):
    return render(request,'regpage.html',context={})
