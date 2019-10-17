from django.contrib import admin

from django.contrib import admin


from .models import Attraction


class AttractionAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'modified']
    search_fields = ['name', 'created', 'modified']


admin.site.register(Attraction, AttractionAdmin)
