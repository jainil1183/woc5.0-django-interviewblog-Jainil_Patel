# Generated by Django 4.1.5 on 2023-01-31 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0005_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=200, null=True)),
                ('program', models.CharField(max_length=200, null=True)),
                ('graduation_year', models.IntegerField(null=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
