from django.urls import path
from . import views

urlpatterns = [
    path('queueList/', views.dashboard, name='dashboard'),
]
