from django.db import models
from django.forms import ModelForm
from django.urls import reverse
from django.dispatch import receiver
#
from django.db.models.signals import post_save
#
from datetime import date, datetime
from django.contrib.auth.models import User
# Create your models here.


class Timeslot(models.Model):
    date = models.DateField()
    slot = models.CharField(max_length=50)

    def __str__(self):
        return self.slot

    # def get_absolute_url(self):
    #     return reverse('timeslot_detail', kwargs={'pk': self.pk})


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    timeslots = models.ManyToManyField(Timeslot)
    role = models.CharField(max_length=50)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    #

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    #

    def __str__(self):
        return self.user.username

    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={'profile_id': self.id})


class Photo(models.Model):
    url = models.CharField(max_length=200)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for profile_id: {self.user_id} @{self.url}"
