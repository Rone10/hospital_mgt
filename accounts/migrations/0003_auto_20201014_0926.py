# Generated by Django 3.1.2 on 2020-10-14 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_doctor_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('ANES', 'Anesthetics'), ('CRDLGY', 'Cardiologist'), ('DMRTLGY', 'Dermatologists'), ('RAD', 'Radiology'), ('GYN', 'Gynecology')], default='GYN', max_length=50),
        ),
    ]
