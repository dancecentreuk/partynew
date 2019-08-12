from django.contrib import admin
from .models import Style

# Register your models here.


class StylesAdmin(admin.ModelAdmin):
    list_display = ('id', 'dance_style')
    list_display_links = ('id', 'dance_style')
    list_filter = ('dance_style',)
    prepopulated_fields = {'slug': ('dance_style',)}



admin.site.register(Style, StylesAdmin)
