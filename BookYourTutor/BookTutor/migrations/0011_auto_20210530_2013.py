# Generated by Django 3.1.7 on 2021-05-30 14:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BookTutor', '0010_auto_20210530_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customertutor',
            name='enrollmentDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 30, 14, 28, 9, 843057, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='session',
            name='endDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 14, 28, 9, 844053, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='session',
            name='startDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 30, 14, 28, 9, 844053, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tutorsubjectschedule',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 5, 30, 14, 28, 9, 843057, tzinfo=utc)),
        ),
    ]
