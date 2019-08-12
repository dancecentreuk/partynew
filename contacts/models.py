from django.db import models
from datetime import datetime
from django.urls import reverse

# Create your models here.

class Contact(models.Model):
    booking = models.CharField(max_length=255)
    booking_id = models.IntegerField()
    booking_city=models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    message = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    dance_school = models.CharField(max_length=255)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    contact_city=models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contact:contact-details', kwargs={'contact_id': self.pk})