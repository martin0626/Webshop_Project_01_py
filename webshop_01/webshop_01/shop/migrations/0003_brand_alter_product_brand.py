# Generated by Django 4.0.4 on 2022-05-01 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_category_slug_alter_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.brand'),
        ),
    ]
