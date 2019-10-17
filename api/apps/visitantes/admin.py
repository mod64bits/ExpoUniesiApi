from django.contrib import admin

from .models import VisitorType

class VisitorTypeAdmin(admin.ModelAdmin):
    list_display = ['user', 'visitorName', 'visitorPhone', 'visitorEmail', 'visitorType']
    search_fields = ['user', 'visitorName', 'visitorPhone', 'visitorEmail', 'visitorType']




admin.site.register(VisitorType, VisitorTypeAdmin)