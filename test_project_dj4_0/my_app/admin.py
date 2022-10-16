from django.contrib import admin

from .models import Client


# Register your models here.
@admin.register(Client)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ['name']
