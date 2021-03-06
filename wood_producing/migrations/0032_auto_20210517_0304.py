# Generated by Django 3.1.7 on 2021-05-17 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wood_producing', '0031_auto_20210516_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='importbill',
            name='provider',
        ),
        migrations.AddField(
            model_name='importedmaterial',
            name='quantity',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='importbill',
            name='manager',
            field=models.ForeignKey(blank=True, db_column='Manager', null=True, on_delete=django.db.models.deletion.CASCADE, to='wood_producing.material'),
        ),
        migrations.AlterField(
            model_name='importedmaterial',
            name='materialofprovider',
            field=models.ForeignKey(blank=True, db_column='Materialofprovider', null=True, on_delete=django.db.models.deletion.CASCADE, to='wood_producing.materialofprovider'),
        ),
    ]
