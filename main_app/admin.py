from django.contrib import admin

# Register your models here.
from .models import TimeSlot
from .models import Profile
from .models import Photo



admin.site.register(TimeSlot)
admin.site.register(Profile)
admin.site.register(Photo)


