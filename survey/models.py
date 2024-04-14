from django.db import models
from django.utils import timezone

# Create your models here.

class SurveySection(models.Model):
    name_en = models.CharField(max_length=100)  # English name of the section
    name_zh = models.CharField(max_length=100)  # Chinese name of the section
    code = models.CharField(max_length=10, unique=True)  # Section code NAME of the section
    code_order = models.IntegerField()  # Section NUMBER
    class_name = models.CharField(max_length=100)  # Name of the survey (i.e. class)

    def __str__(self):
        return f"{self.code} - {self.name_en}"  # Using code for identification

class SurveyQuestion(models.Model):
    section_code = models.CharField(max_length=10)  # Store the section code
    section = models.ForeignKey(SurveySection, on_delete=models.CASCADE, related_name='questions')
    text_en = models.TextField()  # English version of the question
    text_zh = models.TextField()  # Chinese version of the question
    question_number = models.IntegerField()  # Unique number for each question within a section
    class_name = models.CharField(max_length=100)  # Name of the survey (i.e. class)

    def __str__(self):
        return f"{self.section.code} - Q{self.question_number} - {self.text_en[:30]}"

class UserResponse(models.Model):
    student_id = models.CharField(max_length=20)  # Use student_id as a unique identifier
    groupClass = models.CharField(blank=True, null=True, max_length=200)
    section_code = models.CharField(max_length=10)  # Reference to section code
    question_number = models.IntegerField()  # Question number in the section
    response = models.IntegerField(default=0)  # Range from -100 to +100
    dateStamp = models.DateTimeField(default=timezone.now)
    class_name = models.CharField(max_length=100)  # Name of the survey (i.e. class)
    
    def __str__(self):
        return f"{self.student_id} - {self.section_code} - Q{self.question_number} - {self.response}"


