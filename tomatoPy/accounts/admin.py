from django.contrib import admin

from .models import Client
from .models import ClientToken

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_update')

#@admin.register(ClientToken)
#class ClientTokenAdmin(admin.ModelAdmin):
#    pass
