# Generated by Django 2.0.8 on 2018-09-27 09:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAccounts', '0003_auto_20180926_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateField(default=datetime.date(2018, 9, 27), verbose_name='date joined'),
        ),
    ]