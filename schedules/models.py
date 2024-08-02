from django.db import models

# Create your models here.
class ScheduleModel(models.Model):
    day_of_week = models.CharField(max_length=200)
    barber_name = models.CharField(max_length=200)
    hour = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200, blank=True)