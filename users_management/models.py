from django.db import models
from django.contrib.auth.models import User
from customers.models import Customer

# Create your models here.


class User_Role(models.Model):
    role_name = models.CharField(max_length=20,unique=True)
    class Meta:
        verbose_name_plural = "User Roles"
    def __str__(self):
        return self.role_name

class Administrator (models.Model):
    first_Name = models.CharField(max_length=20)
    last_Name = models.CharField(max_length=20)
    user = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return (f"{self.last_Name} {self.first_Name}")
