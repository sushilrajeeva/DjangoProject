from django.contrib import admin
from .models import UserDetails

# Register your models here.

@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    """
    Admin configuration for UserDetails model
    """
    list_display = ('username', 'email')
    search_fields = ('username', 'email')
    ordering = ('username',)