from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import GoalList, GoalItem

# Create your views here.

def index(request):
    latest_goallist_list = GoalList.objects.order_by('-id').reverse()[:5]
    context = {'latest_goallist_list': latest_goallist_list}
    return render(request, 'goals/index.html', context)

def detail(request, goallist_id):
    goallist = get_object_or_404(GoalList, pk=goallist_id)
    return render(request, 'goals/detail.html', {'goallist': goallist})


def add(request, goallist_id):
    return HttpResponse("You're adding to %s." % goallist_id)

class ToDoCreate(CreateView):
    model = GoalItem
    fields = ['goal_list', 'goal_item', 'created_date', 'completed']