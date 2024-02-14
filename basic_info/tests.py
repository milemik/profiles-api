from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.test import TestCase
from django.utils import timezone

from basic_info.models import MyBasicInfo, SchoolInfo, WorkExperience


# Create your tests here.


# Test models
class MyBasicInfoTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username="testUser")

    def test_my_basic_info_model(self) -> None:
        with self.assertRaises(IntegrityError) as err:
            MyBasicInfo.objects.create()
        self.assertEqual(err.exception.args[0], "NOT NULL constraint failed: basic_info_mybasicinfo.birth_date")

    def test_my_basic_info_fields(self) -> None:
        MyBasicInfo.objects.create(user=self.user, birth_date="1970-01-01")
        self.assertEqual(1, MyBasicInfo.objects.count())
        self.assertEqual(MyBasicInfo.WorkStatus.UNAVAILABLE, MyBasicInfo.objects.first().current_status)
        self.assertEqual(MyBasicInfo.objects.first().age, timezone.now().year - 1970)


class SchoolInfoTestCase(TestCase):
    def setUp(self) -> None:
        user = User.objects.create(username="testUser")
        self.basic_info = MyBasicInfo.objects.create(user=user, birth_date="1970-01-01")

    def test_school_info_model_init(self) -> None:
        with self.assertRaises(IntegrityError) as err:
            SchoolInfo.objects.create()
        self.assertEqual(err.exception.args[0], "NOT NULL constraint failed: basic_info_schoolinfo.basic_info_id")

    def test_school_info_model_create(self) -> None:
        SchoolInfo.objects.create(basic_info=self.basic_info)
        self.assertEqual(1, SchoolInfo.objects.count())


class WorkExperienceTestCase(TestCase):
    def setUp(self) -> None:
        user = User.objects.create(username="testUser")
        self.basic_info = MyBasicInfo.objects.create(user=user, birth_date="1970-01-01")

    def test_school_info_model_init(self) -> None:
        with self.assertRaises(IntegrityError) as err:
            WorkExperience.objects.create()
        self.assertEqual(err.exception.args[0], "NOT NULL constraint failed: basic_info_workexperience.basic_info_id")

    def test_school_info_model_create(self) -> None:
        WorkExperience.objects.create(basic_info=self.basic_info)
        self.assertEqual(1, WorkExperience.objects.count())
