from django.contrib import admin

# Register your models here.

from .models import Writer, News

@admin.register(Writer)
class Admin(admin.ModelAdmin):
    list_display = ("name","lastname","phone")
    search_fields = ("name","lastname","phone")
    
@admin.register(News)
class MajorAdmin(admin.ModelAdmin):
    list_display = ('name', 'content')
    
