# Generated by Django 3.1.7 on 2021-05-30 12:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BookTutor', '0009_auto_20210414_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customertutor',
            name='enrollmentDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 30, 12, 52, 16, 402635, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='session',
            name='endDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 12, 52, 16, 402635, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='session',
            name='startDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 30, 12, 52, 16, 402635, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tutorsubjectschedule',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 5, 30, 12, 52, 16, 401637, tzinfo=utc)),
        ),
    ]