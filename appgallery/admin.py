from django.contrib import admin

from .models import gallery


# Register your models here.

@admin.register(gallery)
class galleryAdmin(admin.ModelAdmin):
    list_display = ['id','photo','date']