from django import forms
from .models import GoalItem

class GoalItemForm(forms.ModelForm):
        #completed = forms.BooleanField()

        class Meta:
            model = GoalItem
            fields = ('goal_item',)