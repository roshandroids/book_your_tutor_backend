# Generated by Django 3.1.7 on 2021-04-07 13:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BookTutor', '0004_auto_20210401_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='O', max_length=10),
        ),
        migrations.AlterField(
            model_name='customertutor',
            name='enrollmentDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 7, 13, 27, 34, 965617, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='session',
            name='endDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 9, 13, 27, 34, 966593, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='session',
            name='startDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 7, 13, 27, 34, 966593, tzinfo=utc)),
        ),
    ]
