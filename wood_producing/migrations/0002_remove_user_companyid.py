# Generated by Django 3.1.7 on 2021-05-08 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wood_producing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='companyid',
        ),
    ]
