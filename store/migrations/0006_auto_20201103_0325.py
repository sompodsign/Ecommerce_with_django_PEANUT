# Generated by Django 3.0 on 2020-11-03 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=50),
        ),
    ]
