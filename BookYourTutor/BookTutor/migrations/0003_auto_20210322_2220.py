# Generated by Django 3.1.7 on 2021-03-22 16:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BookTutor', '0002_auto_20210310_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customertutor',
            name='enrollmentDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 22, 16, 35, 3, 661959, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='session',
            name='endDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 24, 16, 35, 3, 661959, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='session',
            name='startDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 22, 16, 35, 3, 661959, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subject',
            name='level',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advance', 'Advance')], default='Beginner', max_length=20),
        ),
    ]