"""
URL configuration for learnersurvey project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from survey import views as surveyViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', surveyViews.survey_home, name='home'),
    path('survey/', surveyViews.survey_home, name='survey'),
    path('survey/start/', surveyViews.start_survey, name='start_survey'),
    path('survey/<int:code_order>/', surveyViews.survey_view, name='survey_view'),
    path('survey/submit/<int:code_order>/', surveyViews.submit_survey, name='submit_survey'),
    path('survey/complete/', surveyViews.survey_complete, name='survey_complete'),
    #Next must come LAST is catch all for non-matching URLs
    # other URL patterns
    re_path(r'^.*$', surveyViews.survey_home, name='landing_page'),

]
