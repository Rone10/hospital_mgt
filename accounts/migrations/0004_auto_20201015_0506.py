# Generated by Django 3.1.2 on 2020-10-15 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201014_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='assigned_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.doctor'),
        ),
    ]
