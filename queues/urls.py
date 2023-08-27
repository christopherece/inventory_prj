from django.urls import path
from . import views

urlpatterns = [
    path('queueList/', views.queues, name='queues'),
    path('updateticket/<uuid:id>/', views.updateticket, name='updateticket'),
    path('updatequeue/<uuid:id>/', views.updatequeue, name='updatequeue'),


]
