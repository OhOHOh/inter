from django.contrib import admin
from .models import UserTest, Entry

# Register your models here.

@admin.register(UserTest)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    pass
