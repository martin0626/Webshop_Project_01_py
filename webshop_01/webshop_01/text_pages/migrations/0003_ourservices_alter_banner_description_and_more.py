# Generated by Django 4.0.4 on 2022-07-16 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text_pages', '0002_banner_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('fa_icon', models.CharField(max_length=25)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='banner',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='banner',
            name='second_title',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='banner',
            name='title',
            field=models.CharField(max_length=25),
        ),
    ]
