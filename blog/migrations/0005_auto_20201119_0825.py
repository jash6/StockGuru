# Generated by Django 3.1.1 on 2020-11-19 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='stock',
            name='total',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
