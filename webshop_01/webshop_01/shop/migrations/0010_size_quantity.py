# Generated by Django 4.0.4 on 2022-06-22 09:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_size_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='size',
            name='quantity',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
