# Generated by Django 3.2.9 on 2022-04-26 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitehandler', '0003_ac_service_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='skater_registrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phno', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('fname', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('aadhaar', models.CharField(max_length=12)),
                ('doj', models.DateField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='sitehandler/images/')),
            ],
        ),
    ]
