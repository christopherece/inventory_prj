import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    fname = models.CharField(max_length=200, blank=True, null=True)
    mname = models.CharField(max_length=200, blank=True, null=True)
    lname = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    employee_id = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    department = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    is_vip = models.BooleanField(default=False)
    phone_no = models.IntegerField(max_length=20, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.user.username)

