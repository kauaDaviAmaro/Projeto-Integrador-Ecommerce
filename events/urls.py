from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='event_list'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),    
    path('<int:event_id>/appointment/', views.register, name='event_appointment'),
    path('<int:event_id>/appointment/<date>/', views.register, name='register_event'),
]
