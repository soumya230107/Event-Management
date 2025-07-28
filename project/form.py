from django import forms

from .models import SocialEvent
from .models import SeasonalEvent
from .models import HealthEvent
from .models import EntertainmentEvent
from .models import CorporateEvent
from .models import EducationalEvent
from .models import DandiyaBooking
class SocialEventForm(forms.ModelForm):
    class Meta:
        model = SocialEvent
        fields = ['name', 'email', 'phone', 'event_type', 'no_of_attendees', 'event_date', 'message']

class SeasonalEventForm(forms.ModelForm):
    class Meta:
        model = SeasonalEvent
        fields = ['name', 'email', 'phone', 'event_type', 'no_of_attendees', 'event_date', 'message']

class HealthEventForm(forms.ModelForm):
    class Meta:
        model = HealthEvent
        fields = ['name', 'email', 'phone', 'event_type', 'no_of_attendees', 'event_date', 'message']

class EntertainmentEventForm(forms.ModelForm):
    class Meta:
        model = EntertainmentEvent
        fields = ['name', 'email', 'phone', 'event_type', 'no_of_attendees', 'event_date', 'message']

class CorporateEventForm(forms.ModelForm):
    class Meta:
        model = CorporateEvent
        fields = ['name', 'email', 'phone', 'event_type', 'no_of_attendees', 'event_date', 'message']

class EducationalEventForm(forms.ModelForm):
    class Meta:
        model = EducationalEvent
        fields = ['name', 'email', 'phone', 'event_type', 'no_of_attendees', 'event_date', 'message']
