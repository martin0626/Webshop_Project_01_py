# Generated by Django 4.0.4 on 2022-06-16 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_remove_product_size_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], max_length=2),
        ),
    ]
