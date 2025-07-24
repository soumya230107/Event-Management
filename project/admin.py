from django.contrib import admin

# Register your models here.

from .models import SocialEvent
from .models import SeasonalEvent
from .models import EntertainmentEvent
from .models import HealthEvent
from .models import EducationalEvent
from .models import CorporateEvent

@admin.register(SocialEvent)
class SocialEventAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'event_type', 'event_date', 'no_of_attendees', 'message')
    search_fields = ('name', 'email', 'event_type')
    list_filter = ('event_type', 'event_date')

@admin.register(SeasonalEvent)
class SeasonalEventAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'event_type', 'event_date', 'no_of_attendees', 'message')
    search_fields = ('name', 'email', 'event_type')
    list_filter = ('event_type', 'event_date')

@admin.register(HealthEvent)
class HealthEventAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'event_type', 'event_date', 'no_of_attendees', 'message')
    search_fields = ('name', 'email', 'event_type')
    list_filter = ('event_type', 'event_date')

@admin.register(EntertainmentEvent)
class EntertainmentEventAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'event_type', 'event_date', 'no_of_attendees', 'message')
    search_fields = ('name', 'email', 'event_type')
    list_filter = ('event_type', 'event_date')

@admin.register(CorporateEvent)
class CorporateEventAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'event_type', 'event_date', 'no_of_attendees', 'message')
    search_fields = ('name', 'email', 'event_type')
    list_filter = ('event_type', 'event_date')

@admin.register(EducationalEvent)
class EducationalEventAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'event_type', 'event_date', 'no_of_attendees', 'message')
    search_fields = ('name', 'email', 'event_type')
    list_filter = ('event_type', 'event_date')