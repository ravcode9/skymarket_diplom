from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class CustomUserAdmin(BaseUserAdmin):
    """
    Настраиваемый класс администратора для модели User.

    Расширяет стандартный UserAdmin,
     добавляя дополнительные поля и настройки отображения.
    """

    model = User
    list_display = ('email', 'first_name',
                    'last_name', 'is_staff', 'is_active')
    list_filter = ('role', 'is_active')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': (
            'first_name', 'last_name', 'phone', 'avatar', 'town'
        )}),
        ('Permissions', {'fields': ('role', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name',
                       'last_name', 'phone', 'role', 'is_active')}
         ),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, CustomUserAdmin)
