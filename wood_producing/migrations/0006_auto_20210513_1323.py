# Generated by Django 3.1.7 on 2021-05-13 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wood_producing', '0005_remove_order_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderedproduct',
            name='product',
            field=models.ForeignKey(blank=True, db_column='Product', null=True, on_delete=django.db.models.deletion.CASCADE, to='wood_producing.product'),
        ),
    ]
