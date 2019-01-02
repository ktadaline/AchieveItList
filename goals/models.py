import datetime

from django.db import models
from django.utils import timezone

# Create your models here.



class GoalList(models.Model):
    goal_title = models.CharField(max_length=250)

    def __str__(self):
        return self.goal_title


class GoalItem(models.Model):
    goal_list = models.ForeignKey(GoalList, on_delete=models.CASCADE)
    goal_item = models.CharField(max_length=250)
    created_date = models.DateTimeField('date published')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.goal_item

    def published_in_last_24 (self):
        return self.created_date >= timezone.now() - datetime.timedelta(days=1)
