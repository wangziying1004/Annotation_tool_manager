# Generated by Django 4.2.11 on 2024-04-17 02:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("dataset_application", "0002_alter_dataset_info_manager_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dataset_info",
            name="data_name",
        ),
    ]
