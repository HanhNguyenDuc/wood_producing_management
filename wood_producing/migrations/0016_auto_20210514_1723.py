# Generated by Django 3.1.7 on 2021-05-14 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wood_producing', '0015_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='userid',
            field=models.ForeignKey(db_column='UserID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]