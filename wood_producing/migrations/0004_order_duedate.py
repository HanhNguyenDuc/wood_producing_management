# Generated by Django 3.1.7 on 2021-05-13 11:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wood_producing', '0003_order_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='duedate',
            field=models.DateTimeField(db_column='duedate', default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
