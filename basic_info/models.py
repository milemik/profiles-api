from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from common.models import BaseUUIDModel


class MyBasicInfo(BaseUUIDModel):
    class WorkStatus(models.TextChoices):
        OPEN_FOR_WORK = "open-for-work", "Open for work"
        UNAVAILABLE = "unavailable", "Unavailable"
        ONLY_SMALL_JOBS = "only-small-jobs", "Can accept only small jobs"

    user = models.OneToOneField(User, related_name="basic_info", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    birth_date = models.DateField(null=False, blank=False)
    gender = models.CharField(max_length=1, null=False, blank=False)
    current_status = models.CharField(
        choices=WorkStatus.choices, default=WorkStatus.UNAVAILABLE, max_length=50, null=False, blank=False
    )

    @property
    def age(self) -> int:
        return timezone.now().year - self.birth_date.year

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class SchoolInfo(BaseUUIDModel):
    class SchoolType(models.IntegerChoices):
        ELEMENTARY_SCHOOL = 1
        HIGH_SCHOOL = 2
        COLLAGE_SCHOOL = 3
        COURSE = 4
        OTHER = 5

    basic_info = models.ForeignKey(MyBasicInfo, related_name="school_info", on_delete=models.CASCADE)
    type = models.IntegerField(choices=SchoolType.choices, default=SchoolType.OTHER)
    school_name = models.CharField(max_length=150, null=True, blank=True)
    school_town = models.CharField(max_length=100, null=True, blank=True)
    start_year = models.IntegerField(null=True, blank=True)
    end_year = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ["type", "start_year", "end_year"]


class WorkExperience(BaseUUIDModel):
    basic_info = models.ForeignKey(MyBasicInfo, related_name="work_experience", on_delete=models.CASCADE)
    company = models.CharField(max_length=100, null=False, blank=False)
    role = models.CharField(max_length=100, null=False, blank=False)
    work_description = models.TextField(null=True, blank=True)
    start_year = models.IntegerField(null=True, blank=True)
    end_year = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ["-start_year"]
