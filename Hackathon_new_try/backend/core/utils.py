class Goal:
    ALLOWED_GOALS = ("med_school", "mba", "law_school")  # Define allowed options as a set

    def __init__(self, goal):
        if goal not in self.ALLOWED_GOALS:  # Validate the input
            raise ValueError(f"Invalid goal. Allowed goals are: {', '.join(self.ALLOWED_GOALS)}")
        self.goal = goal
        
class Context:
    ALLOWED_GOALS = ("Pre-College", "Freshman", "Sophomore", "Junior", "Senior") 
    def __init__(self,level):
        if level not in self.ALLOWED_GOALS:
            raise ValueError(f"Invalid level. Allowed levels are: {', '.join(self.ALLOWED_GOALS)}")
        self.level = level
       
class Timeline:
    ALLOWED_GOALS = ("6_months", "1_year", "2_years", "4_year") 
    def __init__(self,time):
        if time not in self.ALLOWED_GOALS:
            raise ValueError(f"Invalid time. Allowed time are: {', '.join(self.ALLOWED_GOALS)}")
        self.time = time
        
class Budget:
    ALLOWED_GOALS = ("low", "medium", "high") 
    def __init__(self,budget):
        if budget not in self.ALLOWED_GOALS:
            raise ValueError(f"Invalid budget. Allowed budget are: {', '.join(self.ALLOWED_GOALS)}")
        self.budget = budget
class gpt_reponse:
    def __init__(self, dict_):
        self.list_of_dict = dict_
        
class coach:
    def __init__(self,id,name,coach_on):
        self.id = id
        self.name = name
        self.coach_on = coach_on
class coaches:
    def __init__(self,coaches:list[coach]):
        self.coaches = coaches


