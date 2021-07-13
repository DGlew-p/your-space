from django.db import models
from django.forms import ModelForm
from django.urls import reverse
from datetime import date, datetime
from django.contrib.auth.models import User
# Create your models here.


class TimeSlot(models.Model):
    date = models.DateField()
    slot = models.CharField(max_length=50)

    def __str__(self):
        return self.date


class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    role = models.TextField(max_length=250)
    timeSlot = models.ManyToManyField(TimeSlot)
    buddy = models.ManyToManyField(User, related_name='buddy', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


def __str__(self):
    return self.user


def get_absolute_url(self):
    return reverse('detail', kwargs={'profile_id': self.id})


class Photo(models.Model):
    url = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for profile_id: {self.profile_id} @{self.url}"
