<<<<<<< HEAD
# Generated by Django 3.2.4 on 2021-07-15 12:06
=======
# Generated by Django 3.2.4 on 2021-07-15 01:50
>>>>>>> 2ea44e2ae6369a5756f8478ba263258346e1957a

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_alter_profile_timeslots'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='timeslots',
            field=models.ManyToManyField(to='main_app.Timeslot'),
        ),
    ]
