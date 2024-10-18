from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='event_list'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),    
]
