# Generated by Django 3.1.7 on 2021-05-15 16:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wood_producing', '0019_auto_20210515_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='update_at',
            field=models.DateTimeField(db_column='update_at', default=datetime.datetime(2021, 5, 15, 16, 5, 44, 325910, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
