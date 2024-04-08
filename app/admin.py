from django.contrib import admin

# Register your models here.

from app.models import Task, Table_com


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass

@admin.register(Table_com)
class Table_comAdmin(admin.ModelAdmin):
    pass