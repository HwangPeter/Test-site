# Generated by Django 2.0.4 on 2018-04-09 04:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plongstatus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='timestamp',
            field=models.CharField(default=datetime.datetime(2018, 4, 8, 21, 22, 55, 535823), editable=False, help_text='Timestamp of last update.', max_length=50),
        ),
    ]
