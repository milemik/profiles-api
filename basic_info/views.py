from rest_framework import serializers
from rest_framework.generics import RetrieveAPIView

from basic_info.models import MyBasicInfo


class BasicInfoView(RetrieveAPIView):
    class MyBasicInfoSerializer(serializers.ModelSerializer):
        class Meta:
            model = MyBasicInfo
            fields = (
                "first_name",
                "last_name",
                "age",
                "gender",
                "current_status",
            )

    queryset = MyBasicInfo.objects.all()
    serializer_class = MyBasicInfoSerializer
