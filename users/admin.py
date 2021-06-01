from django.contrib import admin

from .models import  User, Manager, Parent,GanGroup,contact_model,Video,Gallery

admin.site.register(User)
admin.site.register(Manager)
admin.site.register(Parent)
admin.site.register(contact_model)
admin.site.register(GanGroup)
admin.site.register(Video)
admin.site.register(Gallery)
