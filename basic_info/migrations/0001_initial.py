# Generated by Django 4.2 on 2024-02-10 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="MyBasicInfo",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("birth_date", models.DateField()),
                ("gender", models.CharField(max_length=1)),
                (
                    "current_status",
                    models.CharField(
                        choices=[
                            ("open-for-work", "Open for work"),
                            ("unavailable", "Unavailable"),
                            ("only-small-jobs", "Can accept only small jobs"),
                        ],
                        default="unavailable",
                        max_length=50,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="basic_info",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="WorkExperience",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("company", models.CharField(max_length=100)),
                ("role", models.CharField(max_length=100)),
                ("work_description", models.TextField(blank=True, null=True)),
                ("start_year", models.IntegerField(blank=True, null=True)),
                ("end_year", models.IntegerField(blank=True, null=True)),
                (
                    "basic_info",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="work_experience",
                        to="basic_info.mybasicinfo",
                    ),
                ),
            ],
            options={
                "ordering": ["-start_year"],
            },
        ),
        migrations.CreateModel(
            name="SchoolInfo",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "type",
                    models.IntegerField(
                        choices=[
                            (1, "Elementary School"),
                            (2, "High School"),
                            (3, "Collage School"),
                            (4, "Course"),
                            (5, "Other"),
                        ],
                        default=5,
                    ),
                ),
                (
                    "school_name",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "school_town",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("start_year", models.IntegerField(blank=True, null=True)),
                ("end_year", models.IntegerField(blank=True, null=True)),
                (
                    "basic_info",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="school_info",
                        to="basic_info.mybasicinfo",
                    ),
                ),
            ],
            options={
                "ordering": ["type", "start_year", "end_year"],
            },
        ),
    ]
