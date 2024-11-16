from openai import OpenAI
import config as config
import json
from  utils import Goal, Context, Timeline, Budget
client_id = config.SPOTIFY_CLIENT_ID
client_secret = config.SPOTIFY_CLIENT_SECRET
openAiClient = OpenAI(
    api_key = config.OPENAI_API_KEY,
    organization = config.OPENAI_ORGID
)
class generate_reposnse:
    def __init__(self, Goal, Content, Timeline, Budget):
        self.goal = Goal
        self.content = Content
        self.timeline = Timeline
        self.budget = Budget
    def generate_response(self):
        messages=[]
        with open('general_prompt.txt', 'r') as file:
            content = file.read()
        coaches = json.loads("dummy.json")
        coaches_list = coaches(coaches[self.content['name']])
        system_prompt=content
        messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "system", "content": f"coaches :{coaches_list}" })
        messages.append({"role": "user", "content": f" goal: {self.goal}, content: {self.content}, timeline: {self.timeline}, budget: {self.budget}"})
        
        response = openAiClient.Completion.create(
            model="gpt-4o-mini",
            messages=messages,
        )
        print(response.choices[0].message.content)


goal = Goal("medical_school")
context = Context("sophomore")
timeline = Timeline("1_year")
budget = Budget("Middle")
test_generate = generate_reposnse(goal, context, timeline, budget)
test_generate.generate_response()


