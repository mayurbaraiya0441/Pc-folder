# Generated by Django 5.0.4 on 2024-05-17 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machineapp', '0012_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_image',
            field=models.ImageField(upload_to='customerimage'),
        ),
    ]