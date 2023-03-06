# Generated by Django 4.1.7 on 2023-03-05 18:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleDtls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vehicle_Number', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[A-Za-z][A-Za-z\\d ]*$', 'Only alphanumeric characters are allowed.')])),
                ('Vehicle_Type', models.CharField(choices=[('Two_Wheeler', 'Two Wheeler'), ('Three_Wheeler', 'Three Wheeler'), ('Four_Wheeler', 'Four Wheeler')], default='Two_Wheeler', max_length=15)),
                ('Vehicle_Model', models.TextField(blank=True, null=True)),
                ('Vehicle_Description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
