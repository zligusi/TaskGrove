from django.contrib import admin
from .models import Task 

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'photo', 'description', 'date_completed', 'priority')
    list_filter = ('priority', 'ready', 'date_created', 'date_completed')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']
