# Generated by Django 4.2.16 on 2024-09-07 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_cast'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cast',
            name='birthdate',
        ),
        migrations.RemoveField(
            model_name='cast',
            name='nationality',
        ),
        migrations.RemoveField(
            model_name='crew',
            name='birthdate',
        ),
        migrations.RemoveField(
            model_name='crew',
            name='nationality',
        ),
    ]
