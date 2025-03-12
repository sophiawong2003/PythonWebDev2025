from django.contrib import admin
from django.forms import NumberInput
from django.db import models

# Register your models here.

from .models import Listing     #from models.py file under same directory import class
class ListingAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'is_published', 'price', 'list_date', 'realtor', 'district')
    list_display_links = 'id', 'title'     #multiple tuple no need to add comma
    list_filter = 'realtor',               #single tuple must add comma
    list_editable = 'is_published', 'price', 'district'
    search_fields = 'title', 'description', 'address', 'price'
    list_per_page = 25
    ordering = ['id']
    formfield_overrides = {
        models.IntegerField:{'widget': NumberInput (attrs={'size' : '10'})},}
    

admin.site.register(Listing, ListingAdmin)    #in admin. register class(Listing)
