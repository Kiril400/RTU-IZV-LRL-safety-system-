from django.contrib import admin
from .models import LabUser
from .models import Event
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)

class LabUserAdmin(admin.ModelAdmin):
    list_display = ('card_id', 'username', 'year_grad', 'access_to_lab', 'last_modified', 'date_added')
    search_fields = ['card_id', 'username']
    list_filter = ('access_to_lab', 'last_modified')

class EventAdmin(admin.ModelAdmin):
    list_display = ('time', 'card_id', 'event_type')
    search_fields = ['card_id']
    list_filter = (('event_type', DropdownFilter), 'time',)

admin.site.register(LabUser, LabUserAdmin)
admin.site.register(Event, EventAdmin)