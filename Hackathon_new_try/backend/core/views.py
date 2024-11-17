from django.shortcuts import render
from django.views.generic import View
from django.template.loader import get_template
from core.chatgpt import generate_reposnse
from core.utils import Goal, Context, Timeline, Budget
from core.surveyForms import SurveyForm
import time


class HomeView(View):
    def get(self, request):
        print(get_template('core/home.html'))
        return render(request, 'core/home.html')    
class SurveyView(View):
    def get(self, request):
        # print(get_template('core/survey.html'))
        return render(request, 'core/survey.html')
# class Roadmap(View):
#     def post(self, request, **kwa):
#         form = SurveyForm(request.POST)
#         if form.is_valid():
#             print("This is valid")
#             goal_ = Goal(form.cleaned_data['goal'])
#             context_ = Context(form.cleaned_data['education'])
#             timeline_ = Timeline(form.cleaned_data['timeline'])
#             budget = Budget(form.cleaned_data['budget'])

#         print(goal_)
#         print(context_)
#         print(timeline_)
#         print(budget)
#         chatgpt = generate_reposnse(goal_, context_, timeline_, budget)
#         response =chatgpt.generate_response()
        
#         renderedHTML += "<!DOCTYPE html>\n<html lang=\"en\">\n"
#         renderedHTML += "<body>\n"
#         renderedHTML += "<section class=\"roadmap\">\n"
#         i=1
        
#         for key in response.list_of_dict.keys():
#             renderedHTML += f"<div class='roadmap-item-{i}'>\n"
#             renderedHTML += f"<h2>{i})</h2>\n"
#             print(response.list_of_dict)
#             print(f'key: {key}')
#             dict = response.list_of_dict[key]
            
#             i += 1
#             goals = dict["goal"]
#             actions = dict["action"]
#             coaches = dict["coaches"]
#             renderedHTML += f"<ul>\n"

#             renderedHTML += f"<li>Goal: {goals[0]}</li>\n"
#             renderedHTML += f"<li>Goal: {actions[0]}</li>\n"
#             renderedHTML += f"<li>Goal: {goals[1]}</li>\n"
#             renderedHTML += f"<li>Goal: {actions[1]}</li>\n"
#             renderedHTML += f"<li>Coach: {coaches}</li>\n"

#             renderedHTML += f"</ul>\n"

#             renderedHTML += "</div>\n"

#         renderedHTML += "</section>\n"
#         renderedHTML += "</body>\n"
#         print(get_template('core/roadmap.html'))
#         return render(renderedHTML, 'core/roadmap.html')
class Roadmap(View):
    def post(self, request, **kwargs):
        form = SurveyForm(request.POST)
        time.sleep(5)
        if form.is_valid():
            print("This is valid")
            goal_ = Goal(form.cleaned_data['goal'])
            context_ = Context(form.cleaned_data['education'])
            timeline_ = Timeline(form.cleaned_data['timeline'])
            budget_ = Budget(form.cleaned_data['budget'])

            chatgpt = generate_reposnse(goal_, context_, timeline_, budget_)
            response = chatgpt.generate_response()

            # Assuming response.list_of_dict is a dictionary with your data
            # Pass this data to the template
            context = {
                'roadmap_data': response.list_of_dict
            }

            return render(request, 'core/roadmap.html', context)
