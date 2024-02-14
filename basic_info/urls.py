from django.urls import path

from basic_info.views import BasicInfoView

app_name = "basic_info"


urlpatterns = [
    path("<uuid:pk>/", BasicInfoView.as_view(), name="basic_info"),
]
