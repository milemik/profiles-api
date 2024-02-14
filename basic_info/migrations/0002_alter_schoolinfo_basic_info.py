# Generated by Django 4.2 on 2024-02-14 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("basic_info", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="schoolinfo",
            name="basic_info",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="school_info",
                to="basic_info.mybasicinfo",
            ),
        ),
    ]