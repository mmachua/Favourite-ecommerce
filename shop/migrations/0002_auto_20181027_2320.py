# Generated by Django 2.0.7 on 2018-10-27 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
    ]
