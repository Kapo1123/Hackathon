from openai import OpenAI
import config as config
import json
from core.utils import Goal, Context, Timeline, Budget, coaches
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
        print(response.choices[0].message.content)


goal = Goal("medical_school")
context = Context("sophomore")
timeline = Timeline("2 years")
budget = Budget("Middle")
test_generate = generate_reposnse(goal, context, timeline, budget)
test_generate.generate_response()


