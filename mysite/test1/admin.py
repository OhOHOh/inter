from django.contrib import admin
from .models import Machine, Testset, UserLogin


class UserLoginAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

# Register your models here.

admin.site.register(Machine)
admin.site.register(Testset)
admin.site.register(UserLogin, UserLoginAdmin)
