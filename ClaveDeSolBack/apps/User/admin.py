from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.UserAccount)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',
                    'email', 'is_staff', 'is_coordinador', 'is_admin', 'is_estudiante')
    search_fields = ('first_name', 'last_name',
                     'email', 'is_staff', 'is_coodinador', 'is_admin', 'is_estudiante')
