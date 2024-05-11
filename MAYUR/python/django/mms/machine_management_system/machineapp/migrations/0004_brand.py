# Generated by Django 5.0.4 on 2024-05-09 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machineapp', '0003_alter_category_category_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=200)),
                ('brand_image', models.ImageField(upload_to='categoryimage')),
                ('brand_code', models.CharField(max_length=200)),
                ('brand_status', models.CharField(max_length=200)),
            ],
        ),
    ]