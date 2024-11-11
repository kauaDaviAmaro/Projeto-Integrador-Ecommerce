from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='event_list'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),    
    path('<int:event_id>/appointment/', views.register, name='event_appointment'),
    path('<int:event_id>/appointment/<str:date>/', views.register_appointment, name='register_appointment'),
    path('available_dates/<int:event_id>/<int:year>/<int:month>/', views.get_available_dates, name='get_available_dates'),

]
