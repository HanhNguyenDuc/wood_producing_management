# Generated by Django 3.1.7 on 2021-05-14 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wood_producing', '0014_task_estimated'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(db_column='status', default='Available', max_length=100),
        ),
    ]
