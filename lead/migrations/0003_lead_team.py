# Generated by Django 5.0 on 2024-01-03 23:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lead", "0002_lead_converted_to_client"),
        ("team", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="lead",
            name="team",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="leads",
                to="team.team",
            ),
            preserve_default=False,
        ),
    ]