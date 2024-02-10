from django.contrib import admin

from basic_info.models import MyBasicInfo, SchoolInfo, WorkExperience


class SchoolInfoInlineAdmin(admin.TabularInline):
    model = SchoolInfo
    extra = 1


class WorkExperienceInlineAdmin(admin.TabularInline):
    model = WorkExperience
    extra = 1


@admin.register(MyBasicInfo)
class MyBasicInfoAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "birth_date")
    inlines = (SchoolInfoInlineAdmin, WorkExperienceInlineAdmin)
