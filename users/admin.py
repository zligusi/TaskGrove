from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('avatar', 'display_name', 'username', 'email', 'date_birth')
    search_fields = ('display_name', 'username', 'email')
