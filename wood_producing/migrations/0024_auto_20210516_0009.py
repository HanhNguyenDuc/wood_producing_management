# Generated by Django 3.1.7 on 2021-05-16 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wood_producing', '0023_materialinproduct_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialrequest',
            name='storageid',
            field=models.ForeignKey(db_column='StorageID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wood_producing.storage'),
        ),
    ]
