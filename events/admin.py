from django.contrib import admin
from .models import Event, Appointment

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'event_name', 'date_time')

    def event_name(self, obj):
        return obj.event.name
