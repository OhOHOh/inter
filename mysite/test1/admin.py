from django.contrib import admin
from .models import Machine, Testset, UserLogin, BranchInfo


class UserLoginAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

class BranchInfoAdmin(admin.ModelAdmin):
    list_display = ('branch_name', 'compile_times', 'last_compile', 'run_times', 'last_run')


# Register your models here.

admin.site.register(Machine)
admin.site.register(Testset)
admin.site.register(UserLogin, UserLoginAdmin)
admin.site.register(BranchInfo, BranchInfoAdmin)
