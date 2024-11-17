from django.urls import path
from .views import HomeView, SurveyView, Roadmap

urlpatterns = [
    path('', SurveyView.as_view(), name='story'),
    path('roadmap', Roadmap.as_view(), name='roadmap'),
]