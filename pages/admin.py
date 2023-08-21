from django.contrib import admin
from .models import Category, Items, Location

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        
    )
    list_display_links = ('id', 'name')

admin.site.register(Category, CategoryAdmin)

class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        
    )
    list_display_links = ('id', 'name')

admin.site.register(Location, LocationAdmin)

class ItemsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'serial_no',
        'display_name',
        'stock_room',
        'allocated_to',
        'cost',
        'notes',
        'is_available'

        
    )
    list_display_links = ('id', 'serial_no')

admin.site.register(Items, ItemsAdmin)