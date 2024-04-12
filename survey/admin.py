from django.contrib import admin
from .models import SurveySection, SurveyQuestion, UserResponse

# Register your models here.

@admin.register(SurveySection)
class SurveySectionAdmin(admin.ModelAdmin):
    list_display = ['code', 'code_order', 'name_en', 'name_zh']
    list_filter = ['code', 'code_order', 'name_en']
    ordering = ['code_order', 'code']

@admin.register(SurveyQuestion)
class SurveyQuestionAdmin(admin.ModelAdmin):
    list_display = ['section', 'question_number', 'text_en', 'text_zh']
    list_filter = ['section','question_number','text_en']
    ordering = ['section', 'question_number', 'text_en']

@admin.register(UserResponse)
class UserResponseAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'section_code', 'question_number', 'response', 'dateStamp']
    list_filter = ['question_number', 'student_id','response', 'dateStamp']
    ordering = ['section_code', 'question_number']
