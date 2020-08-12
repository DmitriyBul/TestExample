from django.contrib import admin
from .models import Todolist, Organization

# Register your models here.
admin.site.register(Todolist)
admin.site.register(Organization)