# Generated by Django 4.0.4 on 2022-04-23 18:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sitehandler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='phno',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
