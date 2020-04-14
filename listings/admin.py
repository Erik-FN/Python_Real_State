from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title', 'realtor')
    list_filter = ('realtor', 'is_published')
    list_editable = ('is_published',)
    list_select_related = ('realtor',)
    search_fields = ('title', 'id', 'list_date', 'price', 'realtor__name')


admin.site.register(Listing, ListingAdmin)