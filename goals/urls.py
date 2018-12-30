from django.urls import path
from . import views

app_name = 'goals'
urlpatterns = [

    # ex: /goals/
    path('', views.index, name='index'),
    # ex: /goals/1
    path('<int:goallist_id>', views.detail, name='detail'),
    # ex /goals/1/add/
    path('<int:goallist_id>/add/', views.add, name='add'),

]