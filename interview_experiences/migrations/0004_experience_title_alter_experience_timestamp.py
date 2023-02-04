# Generated by Django 4.1.5 on 2023-01-27 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview_experiences', '0003_alter_experience_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='title',
            field=models.TextField(default='', unique=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
