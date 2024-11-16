from django.shortcuts import render
from django.views.generic import View
from django.template.loader import get_template
from core.chatgpt import generate_reposnse
from core.utils import Goal, Context, Timeline, coach

class HomeView(View):
    def get(self, request):
        print(get_template('core/home.html'))
        return render(request, 'core/home.html')    
class SurveyView(View):
    def get(self, request):
        # print(get_template('core/survey.html'))
        return render(request, 'core/survey.html')
class Roadmap(View):
    def get(self, request, **kwa):
        goal_ = Goal(kwa[Goal])
        context_ = Context(kwa[Context])
        timeline_ = Timeline(kwa[Timeline])
        coach_ = coach(kwa[coach])

        response = generate_reposnse.generate_response(goal_, context_, timeline_, coach_)
        
        renderedHTML = "<!DOCTYPE html><html lang=\"en\">"
        for dict in response:
            renderedHTML += "<div class='bucket'>\n"
            goals = dict.get(goals)
            for goal in goals:
                renderedHTML += f"<p>Goal: {goal}</p>\n"
            actions = dict.get(actions)
            for action in actions:
                renderedHTML += f"<p>Goal: {action}</p>\n"
            coaches = dict.get(coaches)
            for coach in coaches:
                renderedHTML += f"<p>Coach: {coach}</p>\n"
            
            renderedHTML += "</div>\n"

        print(get_template('core/roadmap.html'))
        return render(response, 'core/roadmap.html')
