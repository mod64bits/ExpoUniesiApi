from django.contrib import admin


from .models import Event


class EventsAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'date', 'place']
    search_fields = ['name', 'owner', 'date', 'place']


admin.site.register(Event, EventsAdmin)