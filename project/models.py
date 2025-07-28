from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class SocialEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    event_type = models.CharField(max_length=100)
    no_of_attendees = models.PositiveIntegerField()
    event_date = models.DateField()
    message = models.TextField()

def _str_(self):
        return f"{self.event_type} by {self.name}"
  

class SeasonalEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    event_type = models.CharField(max_length=100)
    no_of_attendees = models.PositiveIntegerField()
    event_date = models.DateField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
   
   
    def _str_(self):
        return f"{self.event_type} by {self.name}"
    
class HealthEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    event_type = models.CharField(max_length=100)
    no_of_attendees = models.PositiveIntegerField()
    event_date = models.DateField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
   
   
    def _str_(self):
        return f"{self.event_type} by {self.name}"


class EntertainmentEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    event_type = models.CharField(max_length=100)
    no_of_attendees = models.PositiveIntegerField()
    event_date = models.DateField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
   
   
    def _str_(self):
        return f"{self.event_type} by {self.name}"


class CorporateEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    event_type = models.CharField(max_length=100)
    no_of_attendees = models.PositiveIntegerField()
    event_date = models.DateField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
   
   
    def _str_(self):
        return f"{self.event_type} by {self.name}"


class EducationalEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    event_type = models.CharField(max_length=100)
    no_of_attendees = models.PositiveIntegerField()
    event_date = models.DateField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
   
   
    def _str_(self):
        return f"{self.event_type} by {self.name}"

class DandiyaBooking(models.Model):
    SERVICE_CHOICES = [
        ('Costume Booking', 'Costume Booking'),
        ('Costume Purchase', 'Costume Purchase'),
        ('Hall Booking', 'Hall Booking'),
    ]

    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    datetime = models.DateTimeField()

    def __str__(self):
        return f"{self.service} on {self.datetime.strftime('%Y-%m-%d %H:%M')}"
