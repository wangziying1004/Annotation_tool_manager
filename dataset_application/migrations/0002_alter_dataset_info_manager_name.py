# Generated by Django 4.2.11 on 2024-04-02 03:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dataset_application", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dataset_info",
            name="manager_name",
            field=models.CharField(max_length=30),
        ),
    ]