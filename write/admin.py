from django.contrib import admin

# Register your models here.

from .models import Writer, News

@admin.register(Writer)
class Admin(admin.ModelAdmin):
    list_display = ("name","lastname")
    search_fields = ("name","lastname")
    
@admin.register(News)
class MajorAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'by')
    
