from django.db import models
from django.utils import timezone

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    duration = models.DurationField()
    date_created = models.DateTimeField(auto_now_add=True)


class Appointment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_phone = models.CharField(max_length=15, null=True, blank=True) 
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.event.name} on {self.date_time}"
    
    
