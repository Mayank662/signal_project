from django.contrib import admin

# Register your models here.
from .models import Model1, Model2, Model3

admin.site.register(Model1)
admin.site.register(Model2)
admin.site.register(Model3)