from django.contrib import admin
from .models import BranchInfo, Testcase

# Register your models here.

class BranchInfoAdmin(admin.ModelAdmin):
    list_display = ('branch_name', 'compile_times', 'last_compile', 'run_times', 'last_run')


admin.site.register(BranchInfo, BranchInfoAdmin)
admin.site.register(Testcase)

