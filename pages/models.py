from django.db import models
from users.models import Profile

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m%d', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Items(models.Model):

    LOCATION = (
        ('Albany','Albany'),
        ('Albert Street', 'Albert Street'),
        ('CBD East', 'CBD East'),
        ('CBD Other', 'CBD Other'),
        ('Henderson', 'Henderson'),
        ('Manukau', 'Manukau'),
        ('Takapuna/EkePanuku', 'Takapun/EkePanuku'),
        ('TAU', 'TAU'),
        
    )


    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    serial_no = models.CharField(max_length=200)
    display_name =  models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING )
    stock_room = models.CharField(max_length=200, choices=LOCATION, blank=True, null=True)
    allocated_to = models.CharField(max_length=200, blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.display_name
    


