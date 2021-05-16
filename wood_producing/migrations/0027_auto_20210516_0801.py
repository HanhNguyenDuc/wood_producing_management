# Generated by Django 3.1.7 on 2021-05-16 08:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wood_producing', '0026_auto_20210516_0103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='discriminator',
        ),
        migrations.RemoveField(
            model_name='material',
            name='quantity',
        ),
        migrations.AddField(
            model_name='materialrequest',
            name='create_at',
            field=models.DateTimeField(db_column='create_at', default=datetime.datetime(2021, 5, 16, 8, 1, 28, 175716, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='userid',
            field=models.ForeignKey(db_column='UserID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='materialrequest',
            name='taskid',
            field=models.ForeignKey(db_column='TaskID', on_delete=django.db.models.deletion.CASCADE, to='wood_producing.task'),
        ),
    ]
