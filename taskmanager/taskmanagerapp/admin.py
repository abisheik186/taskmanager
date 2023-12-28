from django.contrib import admin
from .models import task_manager_login,tasks
# Register your models here.
admin.site.register(task_manager_login)
admin.site.register(tasks)