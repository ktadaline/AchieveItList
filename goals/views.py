from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the goals index.")


def detail(request, goallist_id):
    return HttpResponse("You're looking at %s." % goallist_id)


def add(request, goallist_id):
    return HttpResponse("You're adding to %s." % goallist_id)
