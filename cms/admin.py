from django.contrib import admin
from .models import *


@admin.register(TasksModel)
class TasksAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']


@admin.register(ImageModel)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['task', ]


@admin.register(CheckListModel)
class CheckListAdmin(admin.ModelAdmin):
    list_display = ['task', 'check']
