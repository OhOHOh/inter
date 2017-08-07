from django.contrib import admin
from .models import Machine, Testset, UserLogin

# Register your models here.

admin.site.register(Machine)
admin.site.register(Testset)
admin.site.register(UserLogin)
