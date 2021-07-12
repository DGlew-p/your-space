from django.contrib import admin

# Register your models here.
from .models import TimeSlot
from .models import Profile
from .models import Photo
from .models import User


admin.site.register(TimeSlot)
admin.site.register(Profile)
admin.site.register(Photo)


