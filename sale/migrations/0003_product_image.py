# Generated by Django 4.0.3 on 2022-03-03 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
    ]
