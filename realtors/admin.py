from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'hire_date', 'email', 'phone', 'is_mvp')
    list_display_links = ('email', 'name')
    search_fields = ('name', 'email', 'phone')
    list_editable = ('is_mvp', )
    list_filter = ('name', 'email', 'phone', 'is_mvp')


admin.site.register(Realtor, RealtorAdmin)

