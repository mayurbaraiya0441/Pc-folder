# Generated by Django 5.0.4 on 2024-05-14 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machineapp', '0007_remove_subcategory_subcategory_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_status',
            field=models.CharField(default='True', max_length=200),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='subcategory_status',
            field=models.CharField(default='True', max_length=200),
        ),
        migrations.AlterField(
            model_name='tax',
            name='tax_status',
            field=models.CharField(default='True', max_length=200),
        ),
    ]
