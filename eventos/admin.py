from django.contrib import admin
from .models import Event, Assistant


# Register your models here.
admin.site.site_header = "Administración de Eventos"
admin.site.site_title = "Panel de Administración de Eventos"
admin.site.index_title = "Bienvenido al Panel de Administración de Eventos"

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('header', 'location', 'start_date', 'end_date')
    search_fields = ('header', 'location')
    list_filter = ('start_date', 'end_date')

@admin.register(Assistant)
class AssistantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'event')
    search_fields = ('name', 'email', 'event__header')
    list_filter = ('event',)