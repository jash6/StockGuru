# Generated by Django 3.1.1 on 2020-11-20 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='ngo',
        ),
    ]
