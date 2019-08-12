from django.contrib import admin


from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'booking', 'booking_id', 'email', 'mobile', )
    list_display_links = ('name',)
    list_filter = ('name', )
    search_fields = ('name',  'special_person', 'dance_style__dance_style',  'booking_notes',)


admin.site.register(Contact, ContactAdmin)
