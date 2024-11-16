from django.shortcuts import render
from django.views.generic import View
from django.template.loader import get_template
class HomeView(View):
    def get(self, request):
        print(get_template('core/home.html'))
        return render(request, 'core/home.html')
    
class SurveyView(View):
    def get(self, request):
        # print(get_template('core/survey.html'))
        return render(request, 'core/survey.html')