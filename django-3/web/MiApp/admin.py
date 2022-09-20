
from django.contrib import admin
from .models import *
# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
   list_display = (
       "type",
       "names",
   )

   search_fields = (
       "type",
       "names",
   )

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Type)
admin.site.register(Category)