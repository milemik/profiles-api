from rest_framework import serializers
from rest_framework.generics import RetrieveAPIView, get_object_or_404

from basic_info.models import MyBasicInfo, SchoolInfo, WorkExperience


class BasicInfoView(RetrieveAPIView):
    class MyBasicInfoSerializer(serializers.ModelSerializer):
        class SchoolInfoSerializer(serializers.ModelSerializer):
            class Meta:
                model = SchoolInfo
                fields = ("type", "school_name", "school_town", "start_year", "end_year")

        class WorkExperienceSerializer(serializers.ModelSerializer):
            class Meta:
                model = WorkExperience
                fields = ("company", "role", "work_description", "start_year", "end_year")

        school_info = SchoolInfoSerializer(many=True, read_only=True)
        work_experience = WorkExperienceSerializer(many=True, read_only=True)

        class Meta:
            model = MyBasicInfo
            fields = ("first_name", "last_name", "age", "gender", "current_status", "school_info", "work_experience")

    serializer_class = MyBasicInfoSerializer
    queryset = MyBasicInfo.objects.all()
