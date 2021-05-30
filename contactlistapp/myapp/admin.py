from django.contrib import admin
from .models import ContactModel

@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'relationship', 'email', 'phone_number', 'address']


    
