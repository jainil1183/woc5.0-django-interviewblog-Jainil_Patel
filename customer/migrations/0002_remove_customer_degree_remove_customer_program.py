# Generated by Django 4.1.5 on 2023-01-21 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='degree',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='program',
        ),
    ]
