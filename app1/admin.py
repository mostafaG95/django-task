from django.contrib import admin

from .models import Car

class CarAdmin(admin.ModelAdmin):
        list_display=['name','description','price']

admin.site.register(Car,CarAdmin)
# Register your models here.
