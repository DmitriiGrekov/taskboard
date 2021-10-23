from django.contrib import admin
from .models import TaskModel, AdvUser


@admin.register(TaskModel)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'title',
                    'date_create',
                    'date_saved',
                    'date_ending')
    list_filter = ('date_ending',)
    list_display_links = ('title',)


@admin.register(AdvUser)
class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('username',
                    'email')
    search_fields = ('username',
                     'email')
