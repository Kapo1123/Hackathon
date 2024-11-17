from django import forms

class SurveyForm(forms.Form):
    GOAL_CHOICES = [
        ('med_school', 'Med School'),
        ('mba', 'MBA'),
        ('law_school', 'Law School'),
    ]
    TIMELINE_CHOICES = [
        ('6_months', '6 Months'),
        ('1_year', '1 Year'),
        ('2_years', '2 Years'),
        ('4_years', '4 Years'),
    ]
    BUDGET_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    EDUCATION_CHOICES = [
        ('Pre-College', 'Pre-College'),
        ('Freshman', 'Freshman'),
        ('Sophomore', 'Sophomore'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
    ]

    goal = forms.ChoiceField(choices=GOAL_CHOICES, label="What is your career goal?")
    timeline = forms.ChoiceField(choices=TIMELINE_CHOICES, label="How long before you want to accomplish your goal?")
    budget = forms.ChoiceField(choices=BUDGET_CHOICES, label="What is your coaching budget?")
    education = forms.ChoiceField(choices=EDUCATION_CHOICES, label="What is your current education level?")
