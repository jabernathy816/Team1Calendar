from django.contrib import admin

from .models import Event


class EventList(admin.ModelAdmin):
    list_display = ('event_name', 'organization', 'contact_number' )
    list_filter = 'organization'
    search_fields = 'organization'
    ordering = ['event_name']

admin.site.register(Event)

