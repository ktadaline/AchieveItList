from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import GoalItemForm
from django.utils import timezone
from django.shortcuts import redirect

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
    if request.method =="POST":
        form = GoalItemForm(request.POST)
        if form.is_valid():
            goalitem = form.save(commit=False)
            goalitem.completed = False
            goalitem.goal_list_id = goallist_id
            goalitem.created_date = timezone.now()
            goalitem.save()
            return redirect('/goals/')
    else:
        form = GoalItemForm()
    return render(request, 'goals/goals_add.html', {'form': form})

def completed(request, goallist_id):
    goallist = get_object_or_404(GoalList, pk=goallist_id)
    try:
            selected_goalitems = goallist.goalitem_set.get(pk=request.POST['goalitem'])
    except (KeyError, GoalItem.DoesNotExist):
        return render(request, 'goals/detail.html',{
            'goallist': goallist,
            'error_message': "You didn't select an item.",
        })
    else:
                selected_goalitems.completed == True
                selected_goalitems.save()
    return HttpResponse(reverse('goals:completed', args=(goallist.id)))


class ToDoCreate(CreateView):
    model = GoalItem
    fields = ['goal_list', 'goal_item', 'created_date', 'completed']