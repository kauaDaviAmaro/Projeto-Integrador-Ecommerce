from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date', 'time')
    search_fields = ('name', 'description', 'date', 'time')

