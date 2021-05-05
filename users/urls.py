from django.urls import path
from .import  views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    #path('regpage.html',views.regpage, name='regpage'),
     path('register/',views.register, name='register'),
     path('parent_register/',views.parent_register, name='parent_register'),
     path('edit_profile/',views.edit_profile, name='edit_profile'),
     path('manager_register/',views.manager_register, name='manager_register'),
     path('login/',views.login_view, name='login'),
     path('profile/',views.profile, name='profile'),
     path('logout/',views.logout_view, name='logout'),
     path('contact/',views.contact_info_view, name='contact'),
     path('contact/delete_contact/<str:parent_name>/',views.delete_contact_view, name='delete_contact'),
     path('change_password/', views.change_password, name='change_password'),
     path('support_page/', views.support_page, name='support_page'),



] +static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
