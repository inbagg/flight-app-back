from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Customer(AbstractUser):
    address = models.CharField(max_length=50, null=True, blank=True)
    phone_no = models.CharField(max_length=20,unique=True, null=True, blank=True)
    role = models.CharField(max_length=255, blank=False, null=False)
    def __str__(self):
        return (f"{self.username}")