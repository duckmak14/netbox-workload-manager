# Generated by Django 5.0.9 on 2024-12-06 01:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_workload_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workloadservice',
            name='workload_cluster',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='netbox_workload_manager.workloadcluster'),
        ),
    ]