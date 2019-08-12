from django.contrib import admin
from .models import Teacher

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'city', )
    list_filter = ('city',)
    list_display_links = ('id', 'first_name')
    search_fields = ('first_name', 'last_name', 'speciality')
    list_per_page = 25

admin.site.register(Teacher, TeacherAdmin)