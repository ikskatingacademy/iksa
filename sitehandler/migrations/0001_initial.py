# Generated by Django 4.0.4 on 2022-04-23 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('mode', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
    ]