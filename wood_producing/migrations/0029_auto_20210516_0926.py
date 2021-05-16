# Generated by Django 3.1.7 on 2021-05-16 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wood_producing', '0028_auto_20210516_0820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materialofprovider',
            name='material',
        ),
        migrations.RemoveField(
            model_name='materialofprovider',
            name='provider',
        ),
        migrations.RemoveField(
            model_name='materialofproviderinstorage',
            name='material',
        ),
        migrations.AlterField(
            model_name='materialofprovider',
            name='importedmaterialid',
            field=models.ForeignKey(db_column='ImportedMaterialID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wood_producing.importedmaterial'),
        ),
    ]
