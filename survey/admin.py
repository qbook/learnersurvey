from django.contrib import admin
from .models import SurveySection, SurveyQuestion, UserResponse

# Register your models here.

@admin.register(SurveySection)
class SurveySectionAdmin(admin.ModelAdmin):
    list_display = ['code', 'code_order', 'name_en', 'name_zh', 'class_name']
    list_filter = ['code', 'code_order', 'name_en', 'class_name']
    ordering = ['class_name', 'code_order', 'code']

@admin.register(SurveyQuestion)
class SurveyQuestionAdmin(admin.ModelAdmin):
    list_display = ['section', 'question_number', 'text_en', 'text_zh', 'class_name']
    list_filter = ['section','question_number','text_en', 'class_name']
    ordering = ['class_name', 'section', 'question_number', 'text_en']

@admin.register(UserResponse)
class UserResponseAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'student_id', 'section_code', 'question_number', 'response', 'dateStamp']
    list_filter = ['class_name', 'question_number', 'student_id','response', 'dateStamp']
    ordering = ['class_name', 'section_code', 'question_number']
