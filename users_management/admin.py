from django.contrib import admin
from .models import User_Role, Administrator

# Register your models here.

admin.site.register(User_Role)
admin.site.register(Administrator)

