# Generated by Django 4.2.13 on 2024-07-18 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_reservation_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='end_date',
            field=models.DateField(null=True),
        ),
    ]
