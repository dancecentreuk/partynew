from django.contrib import admin
from .models import City, Studio, Venue
# Register your models here.



class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_filter = ('name',)

class StudioAdmin(admin.ModelAdmin):
    list_display = ('id', 'studio_name')
    list_display_links = ('id', 'studio_name')
    list_filter = ('studio_name',)

class VenueAdmin(admin.ModelAdmin):
    list_display = ('id', 'venue_name', 'city', 'venue_coordinator' )
    list_display_links = ('id', 'venue_name')
    list_filter = ('venue_name',)


admin.site.register(City, CityAdmin)
admin.site.register(Studio, StudioAdmin)
admin.site.register(Venue, VenueAdmin)