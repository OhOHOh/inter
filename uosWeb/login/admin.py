from django.contrib import admin
from .models import UserLogin

# Register your models here.

class UserLoginAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

admin.site.register(UserLogin, UserLoginAdmin)
