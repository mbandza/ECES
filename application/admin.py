from django.contrib import admin

# Register your models here.

from .models import Etudiant

from django.contrib.admin import AdminSite

from django.contrib.auth.models import User,Group

admin.site.register(Etudiant)
admin.site.unregister(User)
admin.site.unregister(Group)
