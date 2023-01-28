from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

GENDER_CHOICES= [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
    ('Do not wish to disclose', 'Do not wish to disclose'),
    ]

class User(AbstractUser):
    is_Client = models.BooleanField(default=False)
    is_Hospital = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class ClientUser(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name = "Client_user")
    mobile = models.CharField(max_length=15, null=False)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128, null=False, default='Female')
    image = models.ImageField(default = 'default.PNG',upload_to='media')
    def __str__(self):
        return self.user.username

class AdminUser(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name = "admin_user")
    mobile = models.CharField(max_length=15, null=False)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128, null=False, default='Female')
    image = models.ImageField(default = 'default.PNG',upload_to='media')
    def __str__(self):
        return self.user.username

class Hospital(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "Hospital_user")
    mobile = models.CharField(max_length=15, null=False)
    company_name = models.CharField(max_length=300, null=False)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128, null=False, default='Female')
    verified = models.BooleanField(default=False)
    image = models.ImageField(default = 'default.PNG',upload_to='media')
    def __str__(self): 
        return self.user.username