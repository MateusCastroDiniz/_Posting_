# Generated by Django 5.0.2 on 2024-03-11 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posting", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.FileField(blank=True, db_index=True, upload_to=""),
        ),
    ]