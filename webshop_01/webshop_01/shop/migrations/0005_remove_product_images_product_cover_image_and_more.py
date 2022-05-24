# Generated by Django 4.0.4 on 2022-05-21 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_productgallery_product_product_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.AddField(
            model_name='product',
            name='cover_image',
            field=models.ImageField(null=True, upload_to='product_photos'),
        ),
        migrations.AddField(
            model_name='productgallery',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
    ]