from django.db import models
from datetime import datetime
from cities.models import City, Studio, Venue
from styles.models import Style
from teachers.models import Teacher
from django.urls import reverse

# Create your models here.


class Booking(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)
    initial_chat = models.BooleanField(default=False)
    event_date = models.DateField()
    book_before_date = models.DateField()
    start_time= models.CharField(max_length=10, blank=True)
    end_time = models.CharField(max_length=10, blank=True)
    special_person = models.CharField(max_length=80, blank=True)
    dance_style = models.ForeignKey(Style, on_delete=models.DO_NOTHING,)
    dance_style2 = models.ForeignKey(Style, related_name='second_dance', on_delete=models.DO_NOTHING, blank=True, null=True)
    group_size = models.IntegerField(blank=True, null=True)
    enquiry_date = models.DateTimeField(default=datetime.now, blank=True)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    venue_1 = models.ForeignKey(Venue, related_name='potential_venue', on_delete=models.DO_NOTHING, blank=True, null=True)
    venue = models.ForeignKey(Venue, on_delete=models.DO_NOTHING, blank=True, null=True)
    venue_2 = models.ForeignKey(Venue, related_name='backup_venue', on_delete=models.DO_NOTHING, blank=True, null=True)
    confirmed_venue = models.ForeignKey(Venue, related_name='confirmed_venue', on_delete=models.DO_NOTHING, blank=True, null=True)
    venue_booked = models.BooleanField(default=False)
    venue_paid = models.BooleanField(default=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, blank=True, null=True)
    teacher_fee = models.IntegerField(blank=True, null=True)
    teacher_confirmed = models.BooleanField(default=False)
    teacher_texted = models.BooleanField(default=False)
    teacher_paid = models.BooleanField(default=False)
    cost = models.IntegerField(blank=True)
    is_advertised = models.BooleanField(default=False)
    workshop_booked = models.BooleanField(default=False)
    booking_sent = models.BooleanField(default=False)
    deposit_paid = models.BooleanField(default=False)
    agency = models.BooleanField(default=False)
    balance_paid = models.BooleanField(default=False)
    problem = models.BooleanField(default=False)
    booking_notes = models.TextField(blank=True)
    studio = models.ForeignKey(Studio, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bookings:booking', kwargs={'booking_id': self.pk})
