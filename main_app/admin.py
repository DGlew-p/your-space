from django.contrib import admin

# Register your models here.
from .models import Timeslot
from .models import Profile
from .models import Photo



admin.site.register(Timeslot)
admin.site.register(Profile)
admin.site.register(Photo)


