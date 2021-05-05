from django.contrib import admin

from .models import  User, Manager, Parent,GanGroup,contact_model

admin.site.register(User)
admin.site.register(Manager)
admin.site.register(Parent)
admin.site.register(contact_model)
admin.site.register(GanGroup)
