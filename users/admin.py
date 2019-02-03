from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'type']
    list_filter = ['type']
    fieldsets = (
        (None, {'fields': ('username', 'type', 'professor')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active', 'user_permissions')})
    )

    class Media:
        js = ('users/base.js',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'professor':
            kwargs['queryset'] = CustomUser.objects.filter(type='professor')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(CustomUser, CustomUserAdmin)
