from django.contrib import admin

# Register your models here.

from .models import Listing     #from models.py file under same directory import class
admin.site.register(Listing)    #in admin. register class(Listing)
