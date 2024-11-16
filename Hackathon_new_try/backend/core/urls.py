from django.urls import path
from .views import HomeView, SurveyView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('survey', SurveyView.as_view(), name='story'),

]