from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'department', 'role', 'date_joined')
    search_fields = ('name', 'email')
    list_filter = ('department', 'role')
