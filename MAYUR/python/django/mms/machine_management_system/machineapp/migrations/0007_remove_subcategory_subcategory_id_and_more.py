# Generated by Django 5.0.4 on 2024-05-13 10:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machineapp', '0006_subcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='subcategory_id',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='machineapp.category'),
            preserve_default=False,
        ),
    ]