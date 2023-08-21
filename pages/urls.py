from django.urls import path
from . import views
from .views import get_item_data

urlpatterns = [
    path('', views.index, name='index'),
    path('get_item_data/', get_item_data, name='get_modal_data'),
    path('get_all_stockroom/', views.get_all_stockroom, name='get_all_stockroom'),
    path('edit_item/<int:id>/', views.edit_item, name='edit_item'),

]
