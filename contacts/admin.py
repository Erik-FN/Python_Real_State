from django.contrib import admin
from .models import Contact

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('listing', 'listing_id', 'name', 'email', 'realtor_email')

admin.site.register(Contact, ListingAdmin)

