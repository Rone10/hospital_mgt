# Generated by Django 3.1.3 on 2020-12-14 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20201212_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.doctor'),
        ),
    ]
