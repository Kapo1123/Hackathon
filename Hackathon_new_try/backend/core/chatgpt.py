from openai import OpenAI
import os
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")
import config as config
import json
from core.utils import Goal, Context, Timeline, Budget, coaches, gpt_reponse
import os
current_directory = os.getcwd()
print(f"Current Working Directory: {current_directory}")
from openai.types.chat.chat_completion_message_param import ChatCompletionMessageParam
client = OpenAI()
Message = ChatCompletionMessageParam
class generate_reposnse:
    def __init__(self, Goal, Content, Timeline, Budget):
        self.goal = Goal
        self.context = Content
        self.timeline = Timeline
        self.budget = Budget
    def generate_response(self):
        messages=[]
        with open('core/general_prompt.txt', 'r') as file:
            content = file.read()
        with open('core/dummy.json', 'r') as file:
            data = json.load(file)
        # content = data[self.goal.goal]
        coaches_list = coaches(data[self.goal.goal])
        system_prompt=content
        messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "system", "content": f"coaches :{coaches_list}" })
        messages.append({"role": "user", "content": f" Here are the infomation you need to generate my roadmap goal: {self.goal.goal}, content: {self.context.level}, timeline: {self.timeline.time}, budget: {self.budget.budget}"})
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
        )
        data_json = (response.choices[0].message.content)
        data_json = data_json.strip("```").strip()
        data = json.loads(data_json[4:])
        for key in data.keys():
            coach_id = data[key]["coaches"]
            coach_name = coaches_list.coaches[coach_id]["name"]
            data[key]["coaches"]= coach_name
        return_value = gpt_reponse(data)
        return return_value
            



goal = Goal("med_school")
context = Context("Sophomore")
timeline = Timeline("1_year")
budget = Budget("medium")
test_generate = generate_reposnse(goal, context, timeline, budget)
test_generate.generate_response()


