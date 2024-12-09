# Generated by Django 5.0.9 on 2024-11-20 00:40

import django.db.models.deletion
import taggit.managers
import utilities.json
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dcim', '0191_module_bay_rebuild'),
        ('extras', '0121_customfield_related_object_filter'),
        ('tenancy', '0015_contactassignment_rename_content_type'),
        ('virtualization', '0040_convert_disk_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkloadClusterType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkloadCluster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('comments', models.TextField(blank=True)),
                ('contact', models.ManyToManyField(blank=True, default=None, related_name='workload_cluster_contact', to='tenancy.contact')),
                ('devices', models.ManyToManyField(blank=True, default=None, related_name='workload_cluster_device', to='dcim.device')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('virtualmachine', models.ManyToManyField(blank=True, default=None, related_name='workload_clsuter_vm', to='virtualization.virtualmachine')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='netbox_workload_manager.workloadclustertype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkloadService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField(max_length=128)),
                ('application', models.CharField(blank=True, max_length=128, null=True)),
                ('namespace', models.CharField(blank=True, max_length=128, null=True)),
                ('memory', models.PositiveIntegerField(blank=True, null=True)),
                ('cpu', models.PositiveIntegerField(blank=True, null=True)),
                ('gpu', models.PositiveIntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('comments', models.TextField(blank=True)),
                ('contact', models.ManyToManyField(blank=True, default=None, related_name='workload_service_contact', to='tenancy.contact')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
