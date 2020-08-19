from django.db import models
from django.utils import timezone


class Participant(models.Model):
    type_choices = [
        ('BAND', 'Band'),
        ('CARRIAGE', 'Carriage'),
    ]
    name = models.CharField(max_length=50, blank=False, default='')
    manager_email_address = models.CharField(max_length=50, blank=False, default='')
    type_of_participant = models.CharField(max_length=8, choices=type_choices, default='BAND')
    foundation_date = models.DateTimeField()
    registered_date = models.DateTimeField(default=timezone.now())
    order = models.IntegerField(default=1)
