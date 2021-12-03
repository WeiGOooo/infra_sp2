from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'bio', 'username', 'email', 'role')
    search_fields = ('text',)
    empty_value_display = '-пусто-'
