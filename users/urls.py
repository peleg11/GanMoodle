from django.urls import path
from .import  views

urlpatterns=[
    #path('regpage.html',views.regpage, name='regpage'),
     path('register/',views.register, name='register'),
     path('parent_register/',views.parent_register.as_view(), name='parent_register'),
     path('manager_register/',views.manager_register.as_view(), name='manager_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),


]
