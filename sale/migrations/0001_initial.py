# Generated by Django 4.0.3 on 2022-03-01 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('bill', models.IntegerField(blank=True, null=True)),
                ('joining', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
